from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "auth"
urlpatterns = [
    
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('admin', views.admin, name='admin'),
    path('access-denied/<str:issue>', views.access_denied, name="access_denied")
]
