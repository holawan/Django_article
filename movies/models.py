from django.db import models

# Create your models here.

class Movie(models.Model) :
    
    #영화제목
    title = models.CharField(max_length=20)
    #관객 수
    audience = models.IntegerField()
    #개봉일
    release_date= models.DateField()
    #장르
    genre = models.CharField(max_length=30)
    #평점
    score = models.FloatField()
    #포스터 경로
    poster_url = models.TextField()
    #줄거리
    description = models.TextField()

    def __str__(self):
        return f'제목: {self.title} / 평점:{self.score}'
    