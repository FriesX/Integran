"""
URL configuration for our_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from first_app import views
from django.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('first_app/', include('first_app.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('signin/', views.signin, name='signin'),
    path('service/', views.service, name='service'),
    path('team/', views.team, name='team'),
    path('why/', views.why, name='why'),
    path('formpage/', views.signin, name='form_name'),
    path('register/', views.register, name='register'),
]
