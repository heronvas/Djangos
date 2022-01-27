from django.contrib import admin
from django.urls import path
from BlogApp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("signedup", views.signedup, name="signedup"),
    path("loggedin", views.loggedin, name="loggedin"),
    path("blogs", views.blogs, name="blogs"),
    path("logout", views.logout, name="logout"),
    path("admins/addpost", views.addpost, name="addpost"),
    path("postadded", views.postadded, name="postadded"),
    path("blogs/blog/<int:id>", views.showpost, name="showpost"),
    path("yourposts", views.yourposts, name="yourposts"),
    path("admins/updatepost/<int:id>", views.updatepost, name="updatepost"),
    path("updatedone/<int:id>", views.updatedone, name="updatedone"),
    path("aboutauthor", views.aboutauthor, name="aboutauthor"),
    path("updatebio", views.updatebio, name="updatebio"),
    path("bioupdated", views.bioupdated, name="bioupdated"),
    path("blog/blogger/<name>", views.userbio, name="userbio"),
    path("admins/deletepost/<int:id>", views.deletepost, name="deletepost"),
    
    
]

