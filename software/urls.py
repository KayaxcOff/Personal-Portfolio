from django.urls import path
from software.views import software_page

urlpatterns = [
    path('', software_page, name='software-page')
]