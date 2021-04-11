from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_list_or_404, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    RedirectView,
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)

from schemas.models import Schema, Column
from schemas.forms import SchemaForm, ColumnForm

User = get_user_model()


class IndexView(RedirectView):
    url = reverse_lazy('schemas')
    permanent = False


class SchemaListView(LoginRequiredMixin, ListView):
    model = Schema
    template_name = 'schemas/schemas.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class SchemaCreateView(LoginRequiredMixin, CreateView):
    model = Schema
    template_name = 'schemas/new_schema.html'
    form_class = SchemaForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SchemaUpdateView(LoginRequiredMixin, UpdateView):
    model = Schema
    template_name = 'schemas/new_schema.html'
    form_class = SchemaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('configure_schema', kwargs={'pk': pk})
        return success_url


class SchemaDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        schema = get_object_or_404(
            Schema,
            id=kwargs['pk']
        )
        schema.delete()
        return redirect('schemas')
    
    def get(self, request, **kwargs):
        return redirect('index')



class SchemaDetailView(LoginRequiredMixin, DetailView):
    model = Schema
    template_name = 'schemas/configure_schema.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = ColumnForm(self.request.POST or None)
        return data


class ColumnCreateView(LoginRequiredMixin, CreateView):
    model = Column
    form_class = ColumnForm

    def form_valid(self, form):
        form.instance.schema_id = self.kwargs['pk']
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy('configure_schema', kwargs={'pk': pk})
        return success_url        


class ColumnDeleteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        column = get_object_or_404(
            Column,
            id=kwargs['col_pk']
        )
        column.delete()
        return redirect('configure_schema', pk=kwargs['pk'])
    
    def get(self, request, **kwargs):
        return redirect('index')


class GenerateCSV(View):
    pass

"""
    ДОБАВИТЬ ПРОВЕРКУ НА ЮЗЕРА (сейчас пользователь может выйти на чужие айдишники)

    СПРЯТАТЬ SuccessUrl в МИКСИН

    ПОЧИТАТЬ ПО ДИСПАТЧ -- это поможет
    его нужно будет запихнуть в диспатч
"""