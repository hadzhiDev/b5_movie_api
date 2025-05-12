from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

from .yasg import urlpatterns as url_doc

router = DefaultRouter()
router.register('atributes', views.AtrubuteViewset, basename='atributes')


urlpatterns = [
    # path('genres/', views.genre_list, name='genre-list'),
    # path('genres/<int:id>/', views.genre_detail, name='genre-detail'),
    path('genres/', views.GenreListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre-detail'),

    # path('directors/', director_list, name='director-list'),
    # path('directors/<int:id>/', director_detail, name='director-detail'),
    path('movies/', views.movie_list, name='movie-list'),
    path('movies/<int:id>/', views.movie_detail, name='movie-detail'),

    path('auth/', include('api.auth.urls')),
    path('', include(router.urls))
]

urlpatterns += url_doc