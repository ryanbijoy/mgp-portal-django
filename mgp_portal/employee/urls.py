from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('', views.redirect_to_homepage),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.user_logout, name='logout'),
]
