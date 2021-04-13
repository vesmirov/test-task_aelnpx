from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied


class SchemaSuccesUrlMixin:
    def get_success_url(self):
        pk = self.kwargs['pk']
        success_url = reverse_lazy(
            'configure_schema',
            kwargs={'username': self.request.user.username, 'pk': pk}
        )
        return success_url


class UserIsCreatorMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.username != self.kwargs['username']:
            raise PermissionDenied()
        return super().dispatch(request, *args, **kwargs)
