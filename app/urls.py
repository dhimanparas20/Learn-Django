from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('get/', views.get, name="get"),
    path('home/', views.home, name="home"),
    path('name/<name>/', views.name, name="name"),
    path('form/', views.employee_form, name="form"),
    path('form2/', views.employee_form2, name="form2"), 
    path('show/', views.show, name="show"), 
    path('update/', views.update, name="update"), 
    path('delete/', views.delete, name="delete"), 
    path('register/', views.register, name="register"), 
    path('login/', views.login, name="login"), 
    path('logout/', views.logout, name="logout"), 
]

