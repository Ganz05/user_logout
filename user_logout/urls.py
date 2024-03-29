"""
URL configuration for user_logout project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',register,name='register'),
    path('userlogin',userlogin,name='userlogin'),
    path('home',home,name='home'),
    path('userlogout',userlogout,name='userlogout'),
    path('change_password',change_password,name='change_password'),
    path('forget_password',forget_password,name='forget_password'),
    path('view_profile',view_profile,name='view_profile')


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
