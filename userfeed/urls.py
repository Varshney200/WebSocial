from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.userHome,name="userhome"),
    path('post',views.post,name="post"),
    path("delete/<int:postId>",views.delPost,name="delPost"),
    path("<str:username>",views.userProfile,name="userprofile"),
]
