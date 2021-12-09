from django.db import models
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, upload_to='%Y/%m/%d/')

    def __str__(self):
        return self.title