from django.urls import path
from about_me.views import about_me

urlpatterns = [
    path('', about_me, name='about_me')
]