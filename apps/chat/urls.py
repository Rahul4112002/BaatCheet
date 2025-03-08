
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.ChatRoom, name='chat'),
    path('<str:username>/get_messages/', views.get_messages, name='get_messages'),  # API for fetching messages
]
