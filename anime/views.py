from django.shortcuts import render, redirect
from .models import AnimeCharacter
from django.utils.text import slugify

def home(request): 
    return render(request, "index.html")


def character(request, id):
    character = AnimeCharacter.objects.get(id=id)
    name = slugify(character.name)
    return render(request, "character.html", {"character": character, "name": name})


