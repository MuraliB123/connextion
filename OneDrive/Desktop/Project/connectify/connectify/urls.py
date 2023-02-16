"""connectify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from home import views
from home import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
  
    path('services/', views.h),
    path('contact/',data.contact),
    path('about/', views.about),
    path('login/', views.login),
    path('profile/',data.profile),
    path('tutor_register/',views.tutor_register),
    path('create/',data.create),
    path('viewprofile/',data.viewprofile),
    path('terms/',views.terms),
    path('profilee/',views.profilee),
    path('repair/',views.repair),
    path('sports/',views.sports),
    path('restaurant/',views.restaurant),
    path('housekeep/',views.housekeep),
    path('baby/',views.baby),
    path('education/',views.education),
    path('beauty/',views.beauty),
    path('needs/',views.needs),
    path('loans/',views.loans),
    path('doctor/',views.doctor),
    path('land/',data.land),
    path('doct1/',views.doct1),
    path('search/',data.search),
    path('verify/',data.verify),
    
    
    
    
]
