from django.urls import path

from schemas.views import IndexView, SchemaView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('schemas/', SchemaView.as_view(), name='schemas'),
]

# /schemas/
# /schemas/new/
# /schemas/<int: schema_id>/
# /schemas/<int: schema_id>/edit/
# /schemas/<int: schema_id>/delete/
# /schemas/<int: schema_id>/datasets/
# /schemas/<int: schema_id>/datasets/generate/
# /schemas/<int: schema_id>/datasets/<int: dataset_id>/download/