from django.conf import settings
from django.conf.urls import handler404, handler500, handler403
from django.contrib import admin
from django.urls import path, include


handler404 = 'fakedata.errors.page_not_found'  # noqa: F811
handler500 = 'fakedata.errors.server_error'  # noqa: F811
handler403 = 'fakedata.errors.forbidden'  # noqa: F811

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
]

urlpatterns += [
    path('', include('schemas.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
