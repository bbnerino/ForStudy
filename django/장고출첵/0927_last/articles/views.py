from .forms import MovieForm
from django.shortcuts import get_object_or_404, render,redirect
from .models import Movie
from django.views.decorators.http import require_http_methods,require_POST,require_safe
# Create your views here.

@require_safe
def index(request):
    movies = Movie.objects.all()
    context ={
        'movies':movies
    }
    return render(request,'articles/index.html',context)

@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST,request.FILES)
        if form.is_valid():
            movie =form.save()
            return redirect('articles:detail',movie.pk)
    else:
        form = MovieForm()
    context={
        'form':form
    }
    return render(request,'articles/form.html',context)

@require_safe
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context={
        'movie':movie
    }
    return render(request,'articles/detail.html',context)

@require_http_methods(['POST','GET'])
def update(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.method =='POST':
        form =MovieForm(request.POST,request.FILES,instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('articles:detail', movie.pk)
    else:
        form = MovieForm(instance=movie)
    context = {
        'form':form
    }
    return render(request,'articles/form.html',context)

@require_POST
def delete(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    movie.delete()
    return redirect('articles:index')


