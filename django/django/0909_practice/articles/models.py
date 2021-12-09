from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    # upload_to 옵션이 없으면
    # settings.py의 MEDIA_ROOT에 설정한 폴더에 저장된다.
    # upload_to 옵션이 있으면? upload_to = 'uploaded_files'
    # /media/uploaded_files/ 에 저장된다.
    # upload_to='%Y/%m/%d/' -> media/2021/09/09/ 
    # 지금 저장하려는 이
    image =models.ImageField(blank=True,upload_to ="%Y/%m/%d/")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

    # str 매직 메서드가 하는 일이 정확하게 뭘까?
    # article = Article.objects.get(pk=pk)
    # print(article)
    # <Article Article.object(1)>
    # 제목
    def __str__(self):
        return self.title