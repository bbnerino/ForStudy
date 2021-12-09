from django.shortcuts import render,redirect
from .models import Movie
from movies import models
from django.contrib import messages
# Create your views here.
def new(request):
    return render(request,'movies/new.html')
    
def create(request):
    title = request.POST.get('title')
    overview = request.POST.get('overview')
    poster_path = request.POST.get('poster_path')
    movie = Movie(title=title, overview=overview, poster_path=poster_path)
    movie.save()
    return redirect('movies:detail', movie.pk)

def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies':movies
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context={
        'movie': movie
    }
    return render(request,'movies/detail.html',context)

def edit(request,pk):
    movie = Movie.objects.get(pk=pk)
    context={
        'movie': movie
    }
    return render(request,'movies/edit.html',context)

def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.overview = request.POST.get('overview')
    movie.poster_path = request.POST.get('poster_path')
    movie.save()
    return redirect('movies:detail', movie.pk)

def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method=="POST":
        movie.delete()
        return redirect('movies:index')
    else:
        messages.warning(request, "권한이 없습니다.")
        # return redirect('movies:index')
    return redirect('movies:detail',movie.pk)