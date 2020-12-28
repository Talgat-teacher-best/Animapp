from django.test import TestCase, Client
from .models import Anime, Manga
from django.urls import reverse
# Create your tests here.
class AnimeTestCase(TestCase):
	def setUp(self):
		Anime.objects.create(title = 'Anime Name', episodes = 25, studia = 'Something')
		Anime.objects.create(title = 'Anime Name2', episodes = 25, studia = 'Something2')
	def create_anime(self, title = 'Anime Title', episodes = 25, studia = 'Something'):
		return Anime.objects.create(title = title, episodes = episodes, studia = studia)


	def test_anime_test(self):
		obj1 = Anime.objects.get(title = 'Anime Name')
		obj2 = Anime.objects.get(title = 'Anime Name2')
		self.assertEqual(obj1.title, 'Anime Name')
		self.assertEqual(obj2.title, 'Anime Name2')
		self.assertEqual(obj1.episodes, 25)
		self.assertEqual(obj2.episodes, 25)
		self.assertEqual(obj1.studia, 'Something')
		self.assertEqual(obj2.studia, 'Something2')
	def test_book_qs(self):
		title = 'Anoter Title'
		episodes = 25
		object1 = self.create_anime(title = title)
		object2 = self.create_anime(title = title)
		qs = Anime.objects.filter(title = title)
		self.assertEqual(qs.count(), 2)

class MangaTestCase(TestCase):
	def setUp(self):
		Manga.objects.create(title = 'Manga Name')
		Manga.objects.create(title = 'Manga Name2')
	def create_manga(self, title = 'Manga Title'):
		return Manga.objects.create(title = title)


	def test_manga_test(self):
		obj1 = Manga.objects.get(title = 'Manga Name')
		obj2 = Manga.objects.get(title = 'Manga Name2')
		self.assertEqual(obj1.title, 'Manga Name')
		self.assertEqual(obj2.title, 'Manga Name2')
	def test_book_qs(self):
		title = 'Anoter Title'
		object1 = self.create_manga(title = title)
		object2 = self.create_manga(title = title)
		qs = Manga.objects.filter(title = title)
		self.assertEqual(qs.count(), 2)

from django.test import SimpleTestCase
from .forms import AnimeForm, MangaForm, CreateUserForm
from .models import Anime, Manga
from django.forms import TextInput
from django.contrib.auth.models import User
from django.urls import resolve
from .views import index2, Instruction, Menu, Game, loginPage, registerPage, logoutUser


class TestUrls(SimpleTestCase):

    def test_index2_url_resolves(self):
        url = reverse('index2')
        self.assertEquals(resolve(url).func, index2)

    def test_Instruction_url_resolves(self):
        url = reverse('Instruction')
        self.assertEquals(resolve(url).func, Instruction)

    def test_Menu_url_resolves(self):
        url = reverse('Menu')
        self.assertEquals(resolve(url).func, Menu)

    def test_Game_url_resolves(self):
        url = reverse('Game')
        self.assertEquals(resolve(url).func, Game)

    def test_logoutUser_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func, logoutUser)

    def test_loginPage_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginPage)

    def test_registerPage_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, registerPage)

class TestForms(SimpleTestCase):
    def test_CreateUserForm(self):
        response = self.client.post("/my/form/", {'something': 'something'})
        self.assertEqual(response.status_code, 200)

class TestForms(SimpleTestCase):

    def test_CreateUserForm(self):
        form = CreateUserForm(data={})
        class Meta:
            model = User
            fields = ['username', 'email', 'password1', 'password2']

    def test_AnimeForm(self):
        form = AnimeForm(data={})
        class Meta:
            model = Anime
            fields = ['name']

    def test_MangaForm(self):
        form = MangaForm(data={})
        class Meta:
            model = Manga
            fields = ['name']

    class TestForms(SimpleTestCase):
        def test_CreateUserForm(self):
            response = self.client.post("/my/form/", {'something': 'something'})
            self.assertEqual(response.status_code, 200)


class TestViews(TestCase):

    def test_loginPage_Post(self):
        client = Client()

        response = client.get(reverse('login'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    
    def test_registerPage_Post(self):
        client = Client()

        response = client.get(reverse('register'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

