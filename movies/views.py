from django.shortcuts import render,redirect
from .models import Movie
# Create your views here.

def index(request) :
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request,'movies/index.html',context)

def new(request) :
    
    return render(request,'movies/new.html')

def create(request) :
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('url')
    description = request.POST.get('description')

    movie = Movie()

    movie.title=title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    movie.save()

    return redirect('movies:index')

def detail(request,pk) :
    movie = Movie.objects.get(pk=pk) 

    context = {
        'movie' : movie,
    }

    return render(request,'movies/detail.html',context)


def delete(request,pk) :
    if request.method == 'POST' : 
        movie = Movie.objects.get(pk=pk)

        movie.delete()
    return redirect( 'movies:index')

def edit(request,pk) :
    movie = Movie.objects.get(pk=pk)

    context = {
        'movie' : movie 
    }
    return render(request,'movies/edit.html',context)

def update(request,pk) :
    movie = Movie.objects.get(pk=pk)
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('url')
    movie.description = request.POST.get('description')
    movie.save()

    return redirect('movies:index')