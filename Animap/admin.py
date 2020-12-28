from django.contrib import admin

# Register your models here.
from .models import Anime, Manga, Author, Genre

admin.site.register(Anime)
admin.site.register(Manga)
admin.site.register(Author)
admin.site.register(Genre)
