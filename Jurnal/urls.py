"""Jurnal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Uspevaimost import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('changeJurnal/', views.changeJurnal),
    path('changeRasp/', views.changeRasp),
    path('addJurnal/', views.addJurnal),
    path("login/", views.loginn),
    path('home/', views.mainn),
    path('home/rasp/', views.rasp),
    path('home/graph/', views.graph),
    path('home/rasp/add/', views.raspAdd),
    path('home/jurnal/', views.jur),
    path('home/jurnal/clas/', views.jurnal),
    path('home/jurnal/clas/add/', views.jurnalAdd),
    path('home/rasp/day/', views.raspDay),
    path('logout/', views.logoutt),
    path('home/teachers/', views.teachers),
    path('home/pupils/', views.pupils),
    path('home/metodists/', views.metodists),
    path('add/', views.addUs),
    path('del/', views.delUser),
    path('addUs/', views.addUser),
    path('home/allInfo/', views.allInfo),
    path('home/notAllInfo/', views.notAllInfo),
    path('home/rasp/raspNextDay/', views.raspNextDay),
    path('home/rasp/raspPrevDay/', views.raspPrevDay),
    path('home/progress/', views.progress),
    path('home/progress/student/', views.progressStudent),
]
