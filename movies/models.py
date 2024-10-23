from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.CharField(max_length=100)
    image = models.ImageField(upload_to='movies/media')


class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.IntegerField(default=1)
    date_of_session = models.DateField()
    quantity_of_tickets = models.IntegerField()
    ticket_price = models.DecimalField(max_digits=5, decimal_places=2)