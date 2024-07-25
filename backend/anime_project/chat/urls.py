# chat/urls.py

from django.urls import path
from . import views

app_name = 'chat'  # Define the namespace

urlpatterns = [
    path('room/', views.room, name='room'),  # Define the 'room' view
]
