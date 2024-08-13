from django.shortcuts import render
from .models import AnimeCharacter

# Create your views here.
def home(request): 
    return render(request, "index.html")

def character(request, pk):
    character = AnimeCharacter.objects.get(id=pk)
    return render(request, "character.html", {"character": character})

    
