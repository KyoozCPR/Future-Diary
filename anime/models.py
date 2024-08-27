from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError

class AnimeCharacter(models.Model):
    description = models.TextField(max_length=500)
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



def clean_email(value):
    if User.objects.filter(email__iexact=value).exists():
       raise ValidationError("Your email address is already in use!", code="invalid")
   
        

class UserManagerCustom(BaseUserManager):

    def create_user(self, username: models.CharField, email: models.EmailField, password: models.CharField=None):
        if not(username) or not(email):
            raise ValueError("Can't create User without required fields!")

        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, username, email, password=None):
        if not(username) or not(email):
            raise ValueError("Can't create User without required fields!")

        
        user = self.model(username, email)
        self.normalize_email(email)
        user.is_admin = True
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):

    username = models.CharField(max_length=30, blank=False, unique=True)
    email    = models.EmailField(max_length=150, blank=False, unique=True, validators=[clean_email])
    is_admin = models.BooleanField(default=False)
    objects  = UserManagerCustom()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']



class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #the models.CASCADE means that if a user is deleted, it deletes also his profile as well
    bio = models.TextField()
    image = models.ImageField(upload_to="media")

    def __str__(self):

       return self.user.username
       
    

