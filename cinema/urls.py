from django.urls import path

from cinema import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='main'),
    path('movie-detail/<int:id>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('get-by-genres/<int:id>/', views.get_by_genres, name='get_by_genres'),
]
