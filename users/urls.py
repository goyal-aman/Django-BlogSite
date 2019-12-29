from django.urls import path
from . import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', users_views.register, name="users-register"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='users-logout'),
    path('profile/', users_views.profile, name='users-profile')
]