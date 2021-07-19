from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name='register'),
    path("login", views.login, name='login'),
    path("templates/about.htm", views.about, name='about'),
    
]
