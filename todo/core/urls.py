from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('signup/',views.SignUp, name='SignUp'),
    path('login/',views.LogIn, name='LogIn'),
    path('logout/', views.LogOut, name='LogOut'),
]
