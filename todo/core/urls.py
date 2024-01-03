from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('signup/',views.SignUp, name='SignUp'),
    path('login/',views.LogIn, name='LogIn'),
    path('logout/', views.LogOut, name='LogOut'),
    path('changePass/', views.ChangePassword, name='ChangePass'),
    path('addTodo/', views.AddToDo, name='Add'),
    path('editTodo/<int:id>', views.EditToDo, name='Edit'),
    path('deleteTodo/', views.DeleteToDo, name='Delete'),
]
