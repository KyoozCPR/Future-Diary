from django.db import models
from django.conf import settings


class AnimeCharacter(models.Model):
    description = models.TextField(max_length=500)
    name = models.CharField(max_length=50)
    image_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_image_url(self):
        return f'{settings.STATIC_URL}{self.image_path}'