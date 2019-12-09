from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "shop"
urlpatterns = [
   
    path('games', views.list_game, name="list_game"),
    path('consoles', views.list_console, name="list_console"),
    path('genres', views.list_genre, name="list_genre"),
    path('companies', views.list_manufacturer, name="list_company"),
    path('games/search-<str:category>-<str:search>', views.list_game_search, name="list_game_search"),
    path('consoles/search-<str:category>-<str:search>', views.list_console_search, name="list_console_search"),
]
