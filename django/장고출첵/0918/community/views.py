from community.models import Movie
from django.shortcuts import get_object_or_404, redirect, render
from .forms import MovieForm

from django.views.decorators.http import require_safe, require_http_methods
# from django.contrib.auth.decorators import login_required
# Create your views here.
@require_safe
def index(request):
    # movies = Movie.objects.all()
    movies = Movie.objects.order_by('-pk')
    context={
        'movies':movies
    }
    return render(request,'community/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('community:detail', movie.pk)
            # return redirect('community:index')
    else:
        form =  MovieForm()
    context ={
        'form':form
    }
    return render(request,'community/form.html',context)
    
@require_safe
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context ={
        'movie':movie
    }
    return render(request,'community/detail.html',context)

@require_http_methods(['GET','POST'])
def update(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.method=="POST":
        form = MovieForm(request.POST,instance= movie)
        if form.is_valid():
            movie = form.save()
            return redirect('community:detail',movie.pk)
    else:
        form = MovieForm(instance= movie)
    context={
        'movie':movie,
        'form':form
    }
    return render(request,'community/form.html',context)

@require_http_methods('POST')
def delete(request,pk):
    movie =get_object_or_404(Movie,pk=pk)
    movie.delete()
    return redirect('community:index')