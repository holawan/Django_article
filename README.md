# PTJ 05



<div style="text-align: right"> 대전_3반_김동완</div>

## 이번 ptj를 통해 배운 내용

1. 데이터를 생성하고, 조회, 수정, 삭제(CRUD)가 가능한 Web Application을 제작할 수 있었습니다. 
2. Django web framework를 통한 데이터를 조작할 수 있었습니다. 
3. ORM을 통한 데이터 핸들링을 할 수 있었습니다. 
4. 관리자 페이지를 통한 데이터 추가, 수정, 삭제를 할 수 있었습니다. 
5. Bootstrap을 통한 html 꾸미기가 가능했습니다. 



### 개발도구

- VSCode
- Google Chrome Browser
- Bootstrap v5
- Django 3.2+

### 요구사항 

커뮤니티 서비스의 게시판 기능 개발을 위한 단계로, 영화 데이터의 생성, 조회, 수정, 삭제 가능
한 어플리케이션을 완성합니다. 해당 기능은 향후 커뮤니티 서비스의 필수 기능으로 사용됩니다.
아래 기술된 사항들은 필수적으로 구현해야 하는 내용입니다.
django 프로젝트 이름은 pjt05, 앱 이름은 movies로 지정합니다. 

## A.Model

정의할 모델 클래스의 이름은 Movie이며, 다음과 같은 정보를 저장합니다.

![model](README.assets/model.PNG)

### 결과

- 문제 접근 방법 :varchar은 옵션에 따라 최대 글자를 조정하고, 익숙하지 않은 데이터 유형은 django Modle field reference를 참고해서 해결하자. 

- code

  ``` html
  <!DOCTYPE html>
  <html lang="ko">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
    <!-- Custom CSS -->
  
    <title>Navbar Footer Test</title>
  </head>
  <body>
    <!-- 01_nav_footer.html -->
    <!-- 768px에 리스트 요소가 햄버거로 될 수 있도록 navbar-expand-lg를 md로 변경  -->
    <!-- 배경을 검은색으로 만들고 스크롤 해도 나오도록 상단에 고정 -->
    <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top ">
      <!-- navbar의 요소들을 flex와 justify-content-between를 이용해 양 끝에 정렬 -->
      <div class="container-fluid  d-flex justify-content-between ">
        <!-- 로고 넣기 -->
        <a class="navbar-brand" href="/../movies/">SSAFY MOIVE</a>
          <div>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
              <ul class="navbar-nav">
                <!-- 각 리스트 요소를 클릭하면 페이지가 전환되게 구현  -->
                <li class="nav-item">
                  <a class="nav-link active" aria-current="page" href="/../movies/">Home</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'movies:recommendations' %}">영화 추천 받기</a>
                </lfixed-bootoom i>
              </ul>
            </div>
          </div>
      </div>
    </nav>
    {% block header %}
    
    
    {% endblock header %}
  
    {% block movies %}
    
    {% endblock movies %}
  
  <!-- 푸터 만들기 -->
    <footer class="d-flex fixed-bottom d-flex justify-content-center align-items-center bg-dark">
      <div class="text-center p-2 text-white me-5">Web-bootstrap PJT, by김동완</div>
      <div class="d-grid gap-2 d-md-block">
        <a href="javascript:window.scrollTo(0,0);"><button class="ml-5 btn btn-primary" type="button">Top</button></a>
      </div>
    </footer>
  
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
  </body>
  </html>
  ```
  
  ```css
  /* 01_nav_footer.css */
  /* 아래에 코드를 작성해 주세요. */
  .logo{
    width: 150px;
  }
  
  
  .nav_header {
    height: 700px;
    background-image: url('images/header.jpg');
    background-size: cover;
  }
  
  ```
  
- 해결 방식 

  1. Navbar 컴포넌트를 이용해 네비게에션 바의 뼈대를 구축했습니다.
  2. navbar 내부를 컨테이너로 만들고 d-flex 내부 요소를 이용해 양 끝에 요소를 정렬했습니다. 
  3. 각 리스트 요소에 href로 하이퍼링크를 줘 페이지가 전환되게 했습니다.
  4. footer에 javascript를 이용해 클릭시 최상단으로 이동하게 구현했습니다.
  
- 이 문제에서 어려웠던 점 

  - 페이지를 상단으로 이동하게 하는 자바스크립 구현
  
- 내가 생각하는 이 문제의 포인트

  - 네비게이션 바 구현, 최상/하단 고정, 페이지 상단으로 이동하게 하는 버튼 구현 
  
- 이 문제의 느낀점

  - 지난 프로젝트를 복기하다보니 쉽게 해결되었다. 점진적으로 발전시켜나가는 것이 중요한 것 가탇. 

## B. index.html

#### 요구사항 : 

i. Bootstrap Card 컴포넌트를 사용해 최소 6개 이상의 영화를 조회합니다.
ii. 영화 포스터 이미지는 https://via.placeholder.com/를 사용하거나
직접 static 파일을 사용해 출력합니다.
iii. 영화 상세 내용은 랜덤 텍스트를 출력하거나 직접 작성합니다.
iv. 영화 포스터를 클릭하면 해당 영화의 다른 스틸 컷을 볼 수 있는
Bootstrap Carousel 컴포넌트가 출력됩니다.

### 결과

- 문제 접근 방법 : static으로 영화를 입력하고, 영화 스틸컷은 static에서 일단 구현하고 나중에  api로 해결하자. 

  ``` html
  {% extends 'base.html' %}
  
  {% block header %}
  {% load static %}
  <header>
    <div id="carouselExampleInterval" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">
        <div class="carousel-item active" data-bs-interval="2000">
          <img src="{% static 'header1.jpg' %}" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="{% static 'header2.jpg' %}" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item" data-bs-interval="2000">
          <img src="{% static 'header3.jpg' %}" class="d-block w-100" alt="...">
        </div>
      </div>
      <!-- 버튼을 클릭하면 위치에 따라 이전, 이후 사진으로 이동한다.  -->
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleInterval" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    {% comment %} <div class="container">
      <a href="https://placeholder.com"><img src="https://via.placeholder.com/840x600" alt=""></a>
    </div> {% endcomment %}
  </header>
  
  {% endblock header %}
  
  {% block movies %}
    <div class="container">
      <section>
        <!-- class = row로 주고, 화면이 sm이하일 때는 1개만 lg 이하일때는 2개 lg 이상일때는 3개가 보이게함  -->
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 ">
          <article >
            <!-- card 컴포넌트를 이용해 영화 사진, 제목, 설명 구현 -->
            <div class="card" data-bs-toggle="modal" data-bs-target="#staticBackdrop1">
              <img src="{% static 'movie1.jpg' %}" class="img-fluid rounded-start" alt="...">
            </div>
            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop1" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">Still Cut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <img src="{% static 'movie1_still.jpg' %}" alt="" style= "width: 466px; height:400px">
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                  </div>
                </div>
              </div>
            </div>
              <div class="card-body">
                <h5 class="card-title">쇼생크 탈출</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </article>
          <article>
            <div class="card" data-bs-toggle="modal" data-bs-target="#staticBackdrop2">
              <img src="{% static 'movie2.jpg' %}" class="img-fluid rounded-start" alt="...">
            </div>
            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop2" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">Still Cut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <img src="{% static 'movie2_still.jpg' %}" alt="" style= "width: 466px; height:400px">
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                  </div>
                </div>
              </div>
            </div>          
              <div class="card-body">
                <h5 class="card-title">죽은 시인의 사회</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </article>
          <article>
            <div class="card" data-bs-toggle="modal" data-bs-target="#staticBackdrop3">
              <img src="{% static 'movie3.jpg' %}" class="img-fluid rounded-start" alt="...">
            </div>
            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop3" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">Still Cut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <img src="{% static 'movie3_still.jpg' %}" alt="" style= "width: 466px; height:400px">
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                  </div>
                </div>
              </div>
            </div>
              <div class="card-body">
                <h5 class="card-title">다크 나이트 라이즈</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </article>
          <article>
            <div class="card" data-bs-toggle="modal" data-bs-target="#staticBackdrop4">
              <img src="{% static 'movie4.jpg' %}" class="img-fluid rounded-start" alt="...">
            </div>
            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop4" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">Still Cut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <img src="{% static 'movie4_still.jpg' %}" alt="" style= "width: 466px; height:400px">
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                  </div>
                </div>
              </div>
            </div>
              <div class="card-body">
                <h5 class="card-title">그랜드 부다페스트 호텔</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </article>
          <article class="col-lg-3 offset-lg-3">
            <div class="card" data-bs-toggle="modal" data-bs-target="#staticBackdrop5">
              <img src="{% static 'movie5.jpg' %}" class="img-fluid rounded-start" alt="...">
            </div>
            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop5" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">Still Cut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <img src="{% static 'movie5_still.jpg' %}" alt="" style= "width: 466px; height:400px">
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                  </div>
                </div>
              </div>
            </div>
              <div class="card-body">
                <h5 class="card-title">Her</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </article>
          <article>
            <div class="card" data-bs-toggle="modal" data-bs-target="#staticBackdrop6">
              <img src="{% static 'movie6.jpg' %}" class="img-fluid rounded-start" alt="...">
            </div>
            <!-- Modal -->
            <div class="modal fade" id="staticBackdrop6" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="staticBackdropLabel">Still Cut</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <img src="{% static 'movie6_still.jpg' %}" alt="" style= "width: 466px; height:400px">
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">닫기</button>
                  </div>
                </div>
              </div>
            </div>
              <div class="card-body">
                <h5 class="card-title">위대한 쇼맨</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
              </div>
          </article>
        </div>
      </section>
    </div>
  {% endblock movies %}
  ```

- 해결 방식 

  1.  static을 로드하고, 영화 이미지를 전송
  6. carousel을 이용한 영화 자동 넘기기
  6. card 배치를 container와 row-col로 해결
  6. 각 카드별 스틸컷이 나오는 이미지 구현하기 
  
- 이 문제에서 어려웠던 점 

  - modal의 사진 조정 
  - 각 카드별 modal 구현 
  
- 내가 생각하는 이 문제의 포인트

  - 카드 이미지를 static으로 불러오고, html에 구현
  
- 이 문제의 느낀점

  - 해결방식을 쓰다보니 쉬워 보이지만, 직접 구현할 때는 매우 시간이 오래 걸렸던 것 같습니다. 



## C.  recommendations.html

#### 요구사항 : 

i. Bootstrap Card 컴포넌트를 사용합니다.
ii. 영화 “쇼생크 탈출”과 비슷한 영화를 추천 받을 수 있도록 API 요청을 보냅니다.
iii. TMDB API로부터 응답 받은 추천 영화 목록 중 랜덤으로 하나를 출력합니다.
iv. 웹 페이지의 viewport 너비 크기에 따라 다음과 같은 레이아웃으로 구성됩니다.
v. 576px 미만 및 이상

- 문제 접근 방법 : python과 api를 이용해서 영화 정보를 받아오고, 페이지에 구현 해보자 

  ``` html
  {% extends 'base.html' %}
  
  
  {% block header %}
  <header class="d-flex flex-column justify-content-center align-items-center text-black fw-bold my-5 mx-5">
    <div class="display-6 mt-5">쇼생크 탈출과 비슷한 영화 추천받기</div>
  </header>    
  {% endblock header %}
  
  {% block movies %}
  
    {% comment %} <div class="container d-flex justify-content-center">
      <div class="row row-cols-1 row-cols-md-2 ">
        <article>
          <div>
            <img src="https://image.tmdb.org/t/p/w500/{{ poster }} " class="card-img-top" alt="...">
          </div>
        </article>
        <article>
          <div class="card-body my-auto">
            <div class="card-title d-flex">
              <div class="pe-2" >{{ title }}</div>
              <div class="badge bg-success text-wrap" >
                {{ vote_average }}
              </div>
            </div>
            <p class="card-text my-0" style="font-size: 12px; ">{{ overview }}</p>
            <p>개봉일 : {{ release_date }}</p>
            <a href="https://www.themoviedb.org/movie/{{ id }}?language=ko" class="btn btn-primary fx-6 my-0">상세정보</a>
          </div>
        </article>
      </div>
    </div> {% endcomment %}
  
  
    <div class="card container d-flex justify-content-center" style="max-width: 540px;">
      <div class="row g-0">
        <div class="col-md-2 mt-5">
          <img src="https://image.tmdb.org/t/p/w500/{{ poster }}" class="img-fluid rounded-start" alt="...">
        </div>
        <div class="col-md-8">
          <div class="card-body">
            <div class="card-title d-flex">
              <div class="pe-2" >{{ title }}</div>
              <div class="badge bg-success text-wrap" >
                {{ vote_average }}
              </div>            
            </div>
            <p class="card-text my-0" style="font-size: 12px; ">{{ overview }}</p>
            <p>개봉일 : {{ release_date }}</p>
            <a href="https://www.themoviedb.org/movie/{{ id }}?language=ko" class="btn btn-primary fx-6 my-0">상세정보</a>
          </div>
      </div>
    </div>
  {% endblock movies %}
  ```
  
- 해결 방식 

  1. python을 이용해 api에 따라 데이터를 가져오고 딕셔너리로 변환 후, html에 넘겨주었습니다.
  1. container와 row-cols를 이용해 요소를 반응형으로 정렬했습니다.
  
- 이 문제에서 어려웠던 점 

  - api크롤링은 비교적 쉽게 진행되었으나, html내부에서 요소를 정렬하는게 어려웠습니다.

- 내가 생각하는 이 문제의 포인트

  - bootstrap 사용 능력
  - api 크롤링을 통해 영화 정보 가져오기
  
- 이 문제의 느낀점

  - 부트스트랩을 오랜만에 다뤄봤더니 시간이 너무 오래걸렸습니다. 그리고, 결국 마음대로 구현할 수 없었습니다. 
  - -> card 컴포넌트를 이용해 수정했더니 잘 수정되었습니다. 





## views.py

```python
from django.shortcuts import render
import requests
import random

def movie_recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
        'region' : 'KR',
        'language' : 'ko',
        'query' : title
    }
    response = requests.get(BASE_URL + path, params = params).json()
    if response['results'] == [] :
        return None
    # 여기에 코드를 작성합니다. 
    movie_id = response['results'][0]['id'] 
    
    BASE_URL_2 = 'https://api.themoviedb.org/3'
    path_2 = f'/movie/{movie_id}/recommendations'
    params_2 = {
        'api_key' : 'bbd81b379a884bf9476fc33b50fdc89b',
        'language' : 'ko'
    }
    response2 = requests.get(BASE_URL_2 + path_2, params = params_2).json()
    # 여기에 코드를 작성합니다.  

    recommend = response2['results']
    recommend_list = []
    for movie in recommend :
        info = [movie['title'],movie['vote_average'],movie['release_date'],movie['overview'],movie['poster_path'],movie['id']]
        recommend_list.append(info)

    return random.choice(recommend_list)

# Create your views here.
def index(request) :
    return render(request,'index.html')


def recommendations(request) :
    rec = movie_recommendation('쇼생크 탈출')
    context = {
        'title' : rec[0],
        'vote_average' : round(rec[1],1),
        'release_date' : rec[2],
        'overview' : rec[3],
        'poster' : rec[4],
        'id' : rec[5]
    }
    return render(request,'recommendations.html',context)
```

## urls

```python
#pjt04
from django.contrib import admin
from django.urls import path, include
from movies import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/',include('movies.urls')),
]
#movies
from django.urls import path
from . import views
app_name = 'movies'
urlpatterns = [
    path('',views.index,name='movies'),
    path('recommendations/',views.recommendations,name='recommendations'),
]
```





### 후기

- python 코드로 도출한 결과를 html에 구현할 수 있다는 점이 좋았습니다. 
- 컨테이너를 마지막 페이지에 정렬하는데 어려움을 겪어서 아쉬웠습니다.
- 지난 프로젝트가 이번 프로젝트에 도움이 많이 되어서 꾸준히 프로젝트를 발전시키는 것의 즐거움을 느꼈습니다.
- final 프로젝트가 기대됩니다. 

