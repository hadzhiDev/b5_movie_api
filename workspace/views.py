from django.shortcuts import render, get_object_or_404, redirect

from cinema.models import Movie, Directer, Genre
from cinema.forms import GenreForm, MovieForm
from workspace.decorators import login_required_custom


@login_required_custom
def workspace_main(request):
    movie_list = Movie.objects.all()
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')

    form = MovieForm()
    genre_list = Genre.objects.all()
    director_list = Directer.objects.all()

    return render(request, 'workspace/index.html', {
        'form': form,
        'director_list': director_list,
        'genre_list': genre_list,
        'movie_list': movie_list,
    })


@login_required_custom
def create_movie(request):
    movie_list = Movie.objects.all()
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')

    form = MovieForm()

    return render(request, 'workspace/create_movie.html', {
        'form': form,
        'movie_list': movie_list, 
    })


@login_required_custom
def edit_movie(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/workspace/')
    
    form = MovieForm(instance=movie)
    
    genre_list = Genre.objects.all()
    director_list = Directer.objects.all()
    return render(request, 'workspace/edit_movie.html', {
        'director_list': director_list,
        'genre_list': genre_list,
        'movie': movie,
        'form': form,
    })


@login_required_custom
def delete_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    movie.delete()
    return redirect('/workspace/')


@login_required_custom
def create_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre_name = form.cleaned_data.get('name')
            print(form.cleaned_data)
            Genre.objects.create(
                name=genre_name
            )
            return redirect('/workspace/')
        
    form = GenreForm()
    return render(request, 'workspace/create_genre.html', {
        'form': form,
    })
