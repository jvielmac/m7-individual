from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'usuarios'

urlpatterns = [
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='usuarios/login.html'),
        name='login'
    ),
    path('logout/', views.usuario_logout, name='logout'),
]
