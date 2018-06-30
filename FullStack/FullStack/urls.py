"""FullStack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include
from First_app import views
urlpatterns = [
    path(r'',views.index,name='index'),
    path(r'first_app/',include('First_app.urls')),
    path('admin/', admin.site.urls),
    path('form',views.formview,name ='Form'),
    path('form1',views.formview1,name ='Form1'),
    path('SignUp',views.register,name ='SignUp'),
    path('login',views.user_login,name ='login'),
    path('logout',views.user_logout,name ='logout'),




]