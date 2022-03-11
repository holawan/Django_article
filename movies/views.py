from django.shortcuts import render,redirect
from .models import Movie
# Create your views here.

def index(request) :
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request,'movies/index.html',context)


def detail(request,pk) :
    movie = Movie.objects.get(pk=pk) 

    context = {
        'movie' : movie,
    }

    return render(request,'movies/detail.html',context)


