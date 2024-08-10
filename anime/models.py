from django.db import models

class AnimeCharacter(models.Model):
    description = models.TextField(max_length=500)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="characters/")

    def __str__(self):
        return self.name