from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from django.utils import timezone


class User(AbstractUser):
    is_decideur = models.BooleanField(default=False)
    is_gestionnaire = models.BooleanField(default=False)
    is_visiteur = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='media/profile_pictures/', blank=True, null=True)
   

    def __str__(self):
        return f"{self.user.username}: {self.first_name} {self.last_name}"


class Ressource(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    mot_cle = RichTextField(blank=True)
    date_en = models.DateField(default=timezone.now)
    action = models.FileField(upload_to='uploads/')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = RichTextField(blank=True)
    image = models.ImageField(upload_to='media/images/')
    date  = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user

class Video(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    date_en = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title

	

class atelier(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    mot_cle = RichTextField(blank=True)
    
    action = models.FileField(upload_to='uploads/')
   
    date_en = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title


class docum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    mot_cle = RichTextField(blank=True)
    
    action = models.FileField(upload_to='uploads/')
    date_en = models.DateField(default=timezone.now)


    def __str__(self):
        return self.title
    
    
class idcateur(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    mot_cle = RichTextField(blank=True)
    action = models.FileField(upload_to='uploads/')
    date_en = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
