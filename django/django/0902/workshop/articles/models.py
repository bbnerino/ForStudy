from django.db import models

# Create your models here.
class Article(models.Model):
    # 제목 내용 생성시간 수정시간
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title