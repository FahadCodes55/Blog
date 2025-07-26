from  django.urls import path
from .import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='Home'),
    path('post/<str:url_id>', views.post, name="Post"),
    path('about/', views.about, name='About'),
    path('contact', views.contact, name='Contact')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)