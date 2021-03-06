from community.forms import MovieForm
from django.shortcuts import get_object_or_404, render,redirect
from .models import Movie
# from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods,require_safe

@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context ={
        'movies':movies
    }
    return render(request,'community/index.html',context)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('community:detail',movie.pk)
    else:
        form = MovieForm()
    context = {
        'form':form
    }
    return render(request,'community/form.html',context)

@require_safe
def detail(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    context = {
        'movie':movie
    }
    return render(request,'community/detail.html',context)

@require_http_methods(['GET','POST'])
def update(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST,instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('community:detail',movie.pk)
    else:
        form = MovieForm(instance=movie)
    context ={
        'form':form,
        'movie':movie
    }
    return render(request,'community/form.html',context)

@require_http_methods(['POST'])
def delete(request,pk):
    movie = get_object_or_404(Movie,pk=pk)
    movie.delete()
    return redirect('community:index')