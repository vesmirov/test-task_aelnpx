from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.forms import LoginForm


urlpatterns = [
    path(
        'login/',
        LoginView.as_view(authentication_form=LoginForm), name='login',
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
]
