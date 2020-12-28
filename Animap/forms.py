from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Anime, Manga
from django import forms

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AnimeForm(ModelForm):
    class Meta:
        model = Anime
        fields = ['title', 'genre', 'author', 'age', 'description', 'episodes', 'studia']

class MangaForm(ModelForm):
    class Meta:
        model = Manga
        fields = ['title', 'genre', 'author', 'age', 'description']