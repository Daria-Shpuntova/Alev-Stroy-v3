from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about', views.About.as_view(), name='about'),
    path('gallery', views.Image.as_view(), name='gallery'),
    path('price', views.Price.as_view(), name='price'),
    path('<slug:slug>', views.Services.as_view(), name='serves'),
    path('<slug>/<remont_slug>', views.Remonts.as_view(), name='remont'),
]

