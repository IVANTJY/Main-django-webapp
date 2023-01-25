# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 13:07:14 2022

@author: itanb
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from.import views

#now import the views.py file into this code



urlpatterns=[
    
  #Basic
  path('', views.app_homepage, name='app_homepage'),
  path('about_us',  views.about_us, name="about_us"),
  path('services',  views.services, name="services"),
  path('contact_us', views.contact_us, name="contact_us"),
  path('register',  views.register, name="register"),
  path('signin',  views.signin, name='signin'), 
  path('loggedin',  views.loggedin, name='loggedin'), 
  path('logout',  views.logout, name='logout'),


  
  #Productions KPI
  path('tableau',  views.tableau, name='tableau'),
  
  
  #Equipment tracking
  # path('Finaltracking',  views.Finaltracking, name='Finaltracking'),
  path('PM',  views.PM, name='PM'),
  path('Changeover',  views.Changeover, name='Changeover'),
  path('Socketmaintenance',  views.Socketmaintenance, name='Socket maintenance'),
  
  
  
  #Admin
  path("admin/", admin.site.urls),
  
    # path('tracking',  views.tracking, name='tracking'),
  
  
  ]




