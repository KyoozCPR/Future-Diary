from django.shortcuts import render
from .models import AnimeCharacter

# Create your views here.
def home(request): 
    return render(request, "index.html")

def character(request, id):
    character = AnimeCharacter.objects.get(id=id)
    return render(request, "character.html", {"character": character})

    
