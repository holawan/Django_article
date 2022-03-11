from django.shortcuts import render,redirect
from .models import Movie
# Create your views here.


def index(request) :
    #sql에 저장된 모든 영화 정보를 쿼리형태로 가져온다. 
    movies = Movie.objects.all()
    #context에 영화정보를 넣어 index.html에 전달한다. 
    context = {
        'movies' : movies
    }
    return render(request,'movies/index.html',context)

def new(request) :
    #새로운 영화게시글을 만들 new.html을 실행한다. 
    return render(request,'movies/new.html')

def create(request) :
    #new에서 넘어온 데이터를 바탕으로 각 항목에 매핑한다. 
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('url')
    description = request.POST.get('description')

    #movie인스턴스를 생성 후 
    movie = Movie()
    # 각 값을 대입하고
    movie.title=title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description
    #저장한다. 
    movie.save()
    #함수 실행이 끝나면 메인페이지로 돌아간다. 
    return redirect('movies:index')

def detail(request,pk) :
    #영화 상세정보를 볼 수 있는 페이지므로 각 영화 게시글별로 고유한 pk값을 같이 받는다. 
    movie = Movie.objects.get(pk=pk) 
    #pk값을 바탕으로 하나의 영화 인스턴스를 movie에 저장한다.
    context = {
        'movie' : movie,
    }

    #해당 영화 정보를 가진 detail.html을 반환한다. 
    return render(request,'movies/detail.html',context)

    
def delete(request,pk) :
    #게시글을 삭제하는 함수이다. 
    if request.method == 'POST' :
        #POST형태로 해당 영화의 Primary key가 전달되면  
        movie = Movie.objects.get(pk=pk)
        #게시글을 삭제한다. 
        movie.delete()
    return redirect( 'movies:index')

def edit(request,pk) :
    #게시글을 수정하는 함수이다. 
    movie = Movie.objects.get(pk=pk)
    #받아온 pk를 바탕으로 movie인스턴스에 저장하고 
    context = {
        'movie' : movie 
    }
    #context에 담아 edit.html로 보낸다. 
    return render(request,'movies/edit.html',context)

    #영화 정보를 update하는 함수이다. 
def update(request,pk) :
    #edit에서 전달한 pk를 바탕으로 해당 인스턴스에 점근한다.
    movie = Movie.objects.get(pk=pk)
    #edit에서 전달한 내용을 바탕으로 수정을 진행하고 저장한다. 
    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('url')
    movie.description = request.POST.get('description')
    movie.save()

    return redirect('movies:index')