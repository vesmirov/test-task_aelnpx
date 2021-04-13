from django.urls import path

from schemas import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path(
        '<str:username>/schemas/',
        views.SchemaListView.as_view(),
        name='schemas'
    ),
    path(
        '<str:username>/schemas/new/',
        views.SchemaCreateView.as_view(),
        name='new_schema'
    ),
    path(
        '<str:username>/schemas/<int:pk>/',
        views.SchemaDetailView.as_view(),
        name='configure_schema'
    ),
    path(
        '<str:username>/schemas/<int:pk>/edit/',
        views.SchemaUpdateView.as_view(),
        name='edit_schema'
    ),
    path(
        '<str:username>/schemas/<int:pk>/delete/',
        views.SchemaDeleteView.as_view(),
        name='delete_schema'
    ),
    path(
        '<str:username>/schemas/<int:pk>/column/',
        views.ColumnCreateView.as_view(),
        name='new_column'
    ),
    path(
        '<str:username>/schemas/<int:pk>/column/<int:col_pk>/delete/',
        views.ColumnDeleteView.as_view(),
        name='delete_column'
    ),
    path(
        '<str:username>/schemas/<int:pk>/datasets/',
        views.DatasetListView.as_view(),
        name='datasets'
    ),
    path(
        '<str:username>/schemas/<int:pk>/datasets/create/',
        views.DatasetCreateView.as_view(),
        name='new_dataset'
    ),
    path(
        '<str:username>/schemas/<int:pk>/datasets/<int:ds_pk>/download/',
        views.DatasetDownloadView.as_view(),
        name='download_dataset'
    ),
    path(
        '<str:username>/schemas/<int:pk>/datasets/<int:ds_pk>/delete/',
        views.DatasetDeleteView.as_view(),
        name='delete_dataset'
    ),
]
