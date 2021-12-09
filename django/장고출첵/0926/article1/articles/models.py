from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    content =models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title