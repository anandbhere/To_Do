from django.urls import path
from . import views

urlpatterns = [
    path('',views.CreateTask.as_view() ),
    path('ViewTask',views.ViewTask.as_view() ),
    path('UpdateTask',views.UpdateTask.as_view() ),
    path('DeleteTask/<int:pk>',views.DeleteTask.as_view() ),
    path('register',views.Register.as_view()),
    path('Login',views.UserLogin.as_view() ),
    path('Logout',views.UserLogout.as_view() ),
    path('Dashboard',views.Dashboard.as_view() ),

]
