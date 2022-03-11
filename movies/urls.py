from django.urls import path,include
from . import views

app_name = 'movies'
urlpatterns = [
    path('',views.index,name= 'index'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete',views.delete,name='delete'),
    path('new/',views.new,name='new'),
    path('create/', views.create, name='create'), 
    # path('<int:pk>/edit', views.edit, name = 'edit')
]