from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    GenericAPIView,
    CreateAPIView,
    ListAPIView, 
    ListCreateAPIView,
    UpdateAPIView,
    RetrieveAPIView, 
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,
    DestroyAPIView,
)

from .serializer import GenreSerializer, Directer, MovieSerializer, MovieReadSerializer
from .paginations import SimpleResultPagination
from cinema.models import Genre, Movie


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()

        paginator = SimpleResultPagination()

        paginated_movies = paginator.paginate_queryset(movies, request)

        serializer = MovieReadSerializer(paginated_movies, many=True)
        
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # pagination_class = SimpleResultPagination


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'GET':
        serializer = MovieReadSerializer(movie)
        return Response(serializer.data)

    if request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = MovieSerializer(movie, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GenreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # lookup_field = 'pk'


class GenreListView(GenericAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, *args, **kwargs):
        genres = self.get_queryset()
        serializer = self.get_serializer(genres, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenreDetailView(GenericAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get(self, request, pk, *args, **kwargs):
        genre = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(genre)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        genre = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
        genre = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(genre, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        genre = get_object_or_404(self.get_queryset(), pk=pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET',])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()

        serializer = GenreSerializer(genres, many=True)

        print(serializer.data)

        return Response(serializer.data)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def genre_detail(request, id):
    genre = get_object_or_404(Genre, id=id)
    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        print(serializer.data.get('name', 'Unknown'))
        return Response(serializer.data)

    
    if request.method in ['PUT', 'PATCH']:
        partial = request.method == 'PATCH'
        serializer = GenreSerializer(genre, data=request.data, partial=partial)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    