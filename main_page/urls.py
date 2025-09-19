from django.urls import path
from main_page.views import main_page
from about_me.views import about_me
from software.views import software_page
from communication.views import communication

urlpatterns = [
    path('', main_page, name='main_page'),
    path('about-me/', about_me, name='about_me'),
    path('software/', software_page, name='software'),
    path('communication/', communication, name='communication')
]