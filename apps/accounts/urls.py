from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', views.user_login, name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/logout/', views.user_logout, name='logout'),
    path('searched/', views.searched, name='search'),
]