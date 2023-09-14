from django.urls import path
from .views import create_movie, create_rating, get_movie

urlpatterns = [
    path('movies/', create_movie, name='create_movie'),
    path('ratings/', create_rating, name='create_rating'),
    path('movies/<int:movie_id>/', get_movie, name='get_movie')
]
