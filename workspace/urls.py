from django.urls import path

from  workspace.views import (
    workspace_main,
    create_movie,
    edit_movie,
    delete_movie,
    create_genre
)

urlpatterns = [
    path('', workspace_main, name='workspace_main'),
    path('create-movie/', create_movie, name='create_movie'),
    path('edit-movie/<int:id>/', edit_movie, name='edit_movie'),
    path('movie-delete/<int:id>/', delete_movie, name='delete_movie'),
    path('create-genre/', create_genre, name='create_genre'),
] 