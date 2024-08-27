from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("character/<int:id>/",views.character, name="character"),
    
]