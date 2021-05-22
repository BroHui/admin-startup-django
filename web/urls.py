# coding: utf-8
from django.urls import path

from web import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('logout/', views.logout),
    path('demo/', views.demo),
]