from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    rank = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return self.title