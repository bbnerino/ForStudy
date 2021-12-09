import articles
from django.shortcuts import render, redirect,get_object_or_404, resolve_url
from .models import Article

# Create your views here.
def index(request):
    # 작성한 모든 게시글을 출력
    # <querySet []> 
    # articles = Article.objects.all()[::-1] # 내림차순
    articles = Article.objects.order_by('-pk') # 내림차순
    # articles = Article.objects.order_by('pk') # 오름차순
    context ={
        'articles':articles
    }
    return render(request,'articles/index.html',context)


def new(request):
    return render(request,'articles/new.html')


def create(request): # 두개의 경로
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    article =Article(title=title, content=content)
    article.save()
    # new로부터 title 과 content를 받아서 저장
    return redirect('articles:detail',article.pk)
    
def detail(request, pk):
    # 첫번째 인자 -> 모델, 두번째 인자 -> 조사 대상
    article = get_object_or_404(Article,pk=pk)
    # article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }

    return render(request,'articles/detail.html',context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =="POST":
        article.delete()
        return redirect('articles:index')
    
    return redirect('articles:detail',article.pk)


def edit(request, pk):
    article =Article.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request,'articles/edit.html',context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail',article.pk)
