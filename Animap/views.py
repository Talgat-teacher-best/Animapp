from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from .forms import  CreateUserForm, AnimeForm, MangaForm
from django.contrib import messages
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.decorators import login_required
from .models import Anime, Manga
from django.views import generic
import random
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def create(request):
	form = AnimeForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = AnimeForm
	context = {
	'form' : form
	}
	return render(request, 'create.html', context)

def create2(request):
	form = MangaForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = MangaForm
	context = {
	'form' : form
	}
	return render(request, 'create2.html', context)


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'accounts/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('index2')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index2')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def SearchAnime(request):
	
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		result = Anime.objects.filter(title__icontains=q)
		context = {'query': q, 'result': result}
		template = 'result.html'
	else:
		template = 'search_anime.html'
		context = {}
	return render(request, template, context)
@login_required(login_url='login')
def SearchManga(request):
	try:
		q = request.GET.get('q')
	except:
		q = None
	if q:
		result = Manga.objects.filter(title__icontains=q)
		context = {'query': q, 'result': result}
		template = 'result2.html'
	else:
		template = 'search_manga.html'
		context = {}
	return render(request, template, context)

@login_required(login_url='login')	
def index2(request):
	num_visits = request.session.get('num_visits', 1)
	request.session['num_visits'] = num_visits + 1

	context = {
	'num_visits': num_visits,
	}
	return render(
		request,
		'index2.html', context=context)
@login_required(login_url='login')	
def Instruction(request):
	return render(
		request, 
		'Instruction.html')
@login_required(login_url='login')
def Menu(request):
	return render(
		request, 
		'Menu.html')
@login_required(login_url='login')
def Anime_Detail(request):
	SearchAnime(request)
	information = Anime.objects.filter(
		)
	return render(
        request,
        'Anime_Detail.html',
        context={'information': information}
        )
@login_required(login_url='login')
def Manga_Detail(request):
	information = Manga.objects.all()
	return render(
        request,
        'Manga_Detail.html',
        context={'information': information,}
        )
msg = ""
@login_required(login_url='login')
def Game(request):
	global naz, pers
	score = 0
	title = ('Код Гиас', 'Берсерк', 'Тетрадь Смерти', 'Евангелион', 'Дневник Будущего', 'Стальной Алхимик')
	character = ('Лелуш Британский', 'Гатс', 'Ягами Лайт', 'Синдзи Икари', 'Юкитэру Амано', 'Эдвард Элрик')
	d = dict(zip(title, character))
	naz, pers = random.choice(list(d.items()))
	return render(request, 'Game.html', {'msg' : msg, 'title' : pers, 'score' : score})

	
def checkans(request):
	Game(request)
	global naz, pers
	score = 0
	answer = request.GET['answer']
	if answer == naz:
		msg = "Правильно ответил"
		score += 1
		Game(request)
	elif answer != naz:
		msg = "Adlet"
		score = 0
	return render(request, 'Game.html', {'msg' : msg, 'title' : pers, 'score' : score})


