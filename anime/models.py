from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

class AnimeCharacter(models.Model):
    description = models.TextField(max_length=500)
    diary = models.TextField(max_length=500)
    name = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    image_path = models.CharField(max_length=255)
    highlight_episode = models.CharField(max_length=150, default="https://www.youtube.com/watch?v=KfznTm8mJA4")

    def __str__(self):
        return self.name
    

    #create a function to return the full image path
    
    def get_image_url(self):
        return f'{settings.STATIC_URL}{self.image_path}'
    
    from django.db import models



    

