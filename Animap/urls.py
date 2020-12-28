from django.urls import path, include
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    url(r'^$', views.index2, name = 'index2'),
    url(r'^Instruction/$', views.Instruction, name='Instruction'),
    url(r'^Menu/$', views.Menu, name="Menu"),
    url(r'SearchAnime/$', views.SearchAnime, name="SearchAnime"),
    path('SearchManga/', views.SearchManga, name="SearchManga"),
    path('Anime_Detail/', views.Anime_Detail, name='Anime_Detail'),
    path('Manga_Detail/', views.Manga_Detail, name='Manga_Detail'),
    path('Game/', views.Game, name='Game'),
    path('checkans/', views.checkans, name='checkans'),
    path('create/', views.create, name="create"),
    path('create2/', views.create2, name="create2"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)