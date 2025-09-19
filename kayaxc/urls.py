"""
URL configuration for kayaxc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# https://kayaxc.me/
# https://kayaxc.me/main-page/
# https://kayaxc.me/about-me/
# https://kayaxc.me/software/
# https://kayaxc.me/communication/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('main_page/', include('main_page.urls')),
    path('about_me/', include('about_me.urls')),
    path('software/', include('software.urls')),
    path('communication/', include('communication.urls'))
]
