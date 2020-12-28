from django.db import models
from django.urls import reverse
# Create your models here.
class Genre(models.Model):
    
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Anime(models.Model):
	picture = models.ImageField(upload_to='upload/to/path')
	title = models.CharField(max_length = 1000, blank=True, null=True)
	genre = models.ManyToManyField(Genre)
	age = models.CharField(max_length = 1000, blank=True, null=True)
	description = models.CharField(max_length = 1000)
	episodes = models.IntegerField(help_text='количество эпизодов имнно в этой части, а не во всех', blank=True, null=True)
	studia = models.CharField(max_length = 1000, blank=True, null=True)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return f'/Animap/{self.id}'
class Manga(models.Model):
	picture = models.ImageField()
	title = models.CharField(max_length = 1000)
	genre = models.ManyToManyField(Genre)
	age = models.CharField(max_length = 1000)
	description = models.CharField(max_length = 10000)
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	def __str__(self):
		return self.title
class Author(models.Model):

    first_name = models.CharField(max_length = 1000)
    last_name = models.CharField(max_length = 1000)
    Age = models.IntegerField()
  
    class Meta:
        ordering = ['last_name', 'first_name']
    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'