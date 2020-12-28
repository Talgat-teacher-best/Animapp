

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='/Animap/', permanent=True)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += [
     path('Animap/', include('Animap.urls')),
] 

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

