from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import Console, Manufacturer, Game, Genre
from itertools import chain
from django.urls import reverse

# Create your views here.


def list_game(request):
    if request.method == "POST" and request.POST['type'] != "all":
        search = request.POST['search']
        category = request.POST['type']
        return redirect("games/search-"+category+"-"+search)
    else:
        games = Game.objects.all()

        # add platform attribute containing game-console Many-to-Many relationship
        for g in games:
            g.platform = g.console.all()

    return render(request, "shop/inventory_list_game.html",
    context={
        "games": games
    })


def list_console(request):
    if request.method == "POST" and request.POST['type'] != "all":
       search = request.POST['search']
       category = request.POST['type']
       return redirect("consoles/search-"+category+"-"+search)
    else:
        consoles = Console.objects.all()

    return render(request, "shop/inventory_list_console.html",
    context={
        "consoles": consoles,
    })

def list_genre(request):
    genres = Genre.objects.all()

    return render(request, "shop/inventory_list_genre.html",
    context={
        "genres": genres,
    })

def list_manufacturer(request):
    manufacturers = Manufacturer.objects.all()

    return render(request, "shop/inventory_list_manufacturer.html",
    context={
        "manufacturers": manufacturers,
    })

def list_game_search(request, category, search):
    if category == 'name':
        games = Game.objects.filter(name__icontains=search)
    elif category == 'genre':
        genre_selected = Genre.objects.filter(name__contains=search)
        genre_id = genre_selected[0].id
        games = Game.objects.filter(genre=genre_id)
    elif category == 'console':
        console_selected = Console.objects.filter(name__contains=search)
        console_id = console_selected[0].id
        games = Game.objects.filter(console=console_id)
    elif category == 'manufacturer':
        manufacturer_selected = Manufacturer.objects.filter(name__contains=search)
        manufacturer_id = manufacturer_selected[0].id
        games = Game.objects.filter(manufacturer=manufacturer_id)
    else:
        return redirect("games")

    return render(request, "shop/inventory_list_game.html",
    context={
        "games": games,
    })

def list_console_search(request, category, search):
    if category == 'name':
        consoles = Console.objects.filter(name__icontains=search)
    elif category == 'manufacturer':
        manufacturer_selected = Manufacturer.objects.filter(name__contains=search)
        manufacturer_id = manufacturer_selected[0].id
        consoles = Console.objects.filter(manufacturer=manufacturer_id)
    else:
        return redirect("consoles")

    return render(request, "shop/inventory_list_console.html",
    context={
        "consoles": consoles,
    })
