from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.http import FileResponse
from django.views import View
from django.views.generic import (
    RedirectView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
)

from schemas.models import Schema, Column, Dataset
from schemas.forms import SchemaForm, ColumnForm, DatasetForm
from schemas.mixins import SchemaSuccesUrlMixin, UserIsCreatorMixin

User = get_user_model()


class IndexView(LoginRequiredMixin, RedirectView):
    """Index page mixin. Now redirects to schemas page"""

    permanent = False

    def get_redirect_url(self, **kwargs):
        url = reverse_lazy(
            'schemas',
            kwargs={'username': self.request.user.username}
        )
        return url


class SchemaListView(LoginRequiredMixin, UserIsCreatorMixin, ListView):
    """User's schemas"""

    model = Schema
    template_name = 'schemas/schemas.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class SchemaCreateView(LoginRequiredMixin, UserIsCreatorMixin, CreateView):
    """Adding new schema"""

    model = Schema
    template_name = 'schemas/new_schema.html'
    form_class = SchemaForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SchemaUpdateView(LoginRequiredMixin, UserIsCreatorMixin,
                       SchemaSuccesUrlMixin, UpdateView):
    """Edit schema"""

    model = Schema
    template_name = 'schemas/new_schema.html'
    form_class = SchemaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit'] = True
        return context


class SchemaDeleteView(LoginRequiredMixin, UserIsCreatorMixin, View):
    """Delete schema (without confirmation)"""

    def post(self, request, *args, **kwargs):
        schema = get_object_or_404(Schema, id=kwargs['pk'])
        schema.delete()
        return redirect('schemas', username=request.user.username)

    def get(self, request, **kwargs):
        return redirect('index')


class SchemaDetailView(LoginRequiredMixin, UserIsCreatorMixin, DetailView):
    """Schema with columns configuration"""

    model = Schema
    template_name = 'schemas/configure_schema.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = ColumnForm(self.request.POST or None)
        return data


class ColumnCreateView(LoginRequiredMixin, UserIsCreatorMixin,
                       SchemaSuccesUrlMixin, CreateView):
    """Create column configured on schema page"""

    model = Column
    form_class = ColumnForm

    def form_valid(self, form):
        form.instance.schema_id = self.kwargs['pk']
        return super().form_valid(form)

    def form_invalid(self, form):
        redirect_url = redirect(
            'configure_schema',
            username=self.request.user.username,
            pk=self.kwargs['pk']
        )
        return redirect_url


class ColumnDeleteView(LoginRequiredMixin, UserIsCreatorMixin, View):
    """Delete column (without confirmation)"""

    def post(self, request, *args, **kwargs):
        column = get_object_or_404(Column, id=kwargs['col_pk'])
        column.delete()
        redirect_url = redirect(
            'configure_schema',
            username=self.request.user.username,
            pk=self.kwargs['pk']
        )
        return redirect_url

    def get(self, request, **kwargs):
        return redirect('index')


class DatasetListView(LoginRequiredMixin, UserIsCreatorMixin, ListView):
    """Datasets of configured schema"""

    model = Dataset
    template_name = 'schemas/datasets.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        schema_id = self.kwargs['pk']
        return queryset.filter(schema__id=schema_id)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['form'] = DatasetForm(self.request.POST or None)
        data['schema'] = get_object_or_404(Schema, id=self.kwargs['pk'])
        return data


class DatasetCreateView(LoginRequiredMixin, UserIsCreatorMixin, CreateView):
    """Create dataset, start csv generation (via Dataset post_save signal)"""

    model = Dataset
    form_class = DatasetForm
    template_name = 'schemas/datasets.html'

    def form_valid(self, form):
        form.instance.schema_id = self.kwargs['pk']
        return super().form_valid(form)

    def form_invalid(self, form):
        redirect_url = redirect(
            'datasets',
            username=self.request.user.username,
            pk=self.kwargs['pk']
        )
        return redirect_url

    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy(
            'datasets',
            kwargs={'username': self.request.user.username, 'pk': pk}
        )
        return success_url


class DatasetDownloadView(LoginRequiredMixin, UserIsCreatorMixin, View):
    """Download dataset's csv file"""

    def get(self, request, **kwargs):
        dataset = get_object_or_404(Dataset, id=kwargs['ds_pk'])
        csv = dataset.csv_file
        if csv:
            return FileResponse(
                csv, as_attachment=True, filename=f'set_{dataset.id}.csv')
        return redirect('datasets', pk=kwargs['pk'])


class DatasetDeleteView(LoginRequiredMixin, UserIsCreatorMixin, View):
    """Remove dataset from list"""

    def post(self, request, *args, **kwargs):
        dataset = get_object_or_404(Dataset, id=kwargs['ds_pk'])
        dataset.delete()
        redirect_url = redirect(
            'datasets',
            username=self.request.user.username,
            pk=self.kwargs['pk']
        )
        return redirect_url

    def get(self, request, **kwargs):
        return redirect('index')
