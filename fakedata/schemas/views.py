from django.contrib.auth import get_user_model
from django.views.generic import RedirectView, ListView, TemplateView
from django.urls import reverse_lazy

User = get_user_model()

class IndexView(RedirectView):
    url = reverse_lazy('schemas')
    permanent = False

class SchemaView(TemplateView):
    template_name = 'schemas/schemas.html'
