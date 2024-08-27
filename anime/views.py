from django.shortcuts import render, redirect
from .models import AnimeCharacter


def home(request): 
    return render(request, "index.html")


def character(request, id):
    character = AnimeCharacter.objects.get(id=id)
    return render(request, "character.html", {"character": character})


