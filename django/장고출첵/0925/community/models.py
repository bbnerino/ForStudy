from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20)
    rating = models.IntegerField()
    content = models.CharField(max_length=50)
    check = models.CharField(max_length=10)
    def __str__(self):
        return self.title