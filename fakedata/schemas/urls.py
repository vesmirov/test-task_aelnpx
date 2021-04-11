from django.urls import path

from schemas import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('schemas/', views.SchemaListView.as_view(), name='schemas'),
    path('schemas/new/', views.SchemaCreateView.as_view(), name='new_schema'),
    path(
        'schemas/<int:pk>/',
        views.SchemaDetailView.as_view(),
        name='configure_schema'
    ),
    path(
        'schemas/<int:pk>/edit/',
        views.SchemaUpdateView.as_view(),
        name='edit_schema'
    ),
    path(
        'schemas/<int:pk>/delete/',
        views.SchemaDeleteView.as_view(),
        name='delete_schema'
    ),
    path(
        'schemas/<int:pk>/column/',
        views.ColumnCreateView.as_view(),
        name='new_column'
    ),
    path(
        'schemas/<int:pk>/column/<int:col_pk>/delete/',
        views.ColumnDeleteView.as_view(),
        name='delete_column'
    ),
]

# schemas/<int:schema_id>/datasets/
# schemas/<int:schema_id>/datasets/generate/
# schemas/<int:schema_id>/datasets/<int: dataset_id>/download/