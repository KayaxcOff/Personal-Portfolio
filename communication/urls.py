from django.urls import path
from communication.views import communication

urlpatterns = [
    path('', communication, name='communication')
]