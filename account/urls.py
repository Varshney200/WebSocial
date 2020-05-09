from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),                #signup page
    path('signup',views.signup,name="signup"),      #when someone registers on the signup page
    path('login',views.user_login,name="login"),    
    path('logout',views.user_logout,name="logout"),
]