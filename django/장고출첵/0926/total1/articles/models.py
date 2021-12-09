from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title