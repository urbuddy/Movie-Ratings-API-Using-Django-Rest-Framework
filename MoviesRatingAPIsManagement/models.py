from django.db import models
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=100)


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.IntegerField()
