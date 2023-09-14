from django.shortcuts import render
from .models import Movie, Rating
from .serializers import MovieSerializer, RatingSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def create_movie(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_rating(request):
    serializer = RatingSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.validated_data['value'] < 1 or serializer.validated_data['value'] > 5:
            return Response({'error': 'Rating value should be between 1 and 5.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_movie(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    ratings = Rating.objects.filter(movie=movie)
    total_ratings = len(ratings)
    if total_ratings == 0:
        average_rating = None
    else:
        total_rating_value = sum([rating.value for rating in ratings])
        average_rating = total_rating_value / total_ratings

    data = {
        'id': movie.id,
        'title': movie.title,
        'rating': average_rating
    }
    return Response(data, status=status.HTTP_200_OK)
