from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

from cinema.models import Movie, Directer, Genre
from cinema.filters import MovieFilter


from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Movie, Genre
from .filters import MovieFilter


class MovieListView(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movie_list'

    paginate_by = 2

    def get_queryset(self):
        search = self.request.GET.get('search')

        queryset = Movie.objects.filter(is_published=True)

        if search:
            queryset = queryset.filter(name__icontains=search)

        filter_set = MovieFilter(self.request.GET, queryset=queryset)
        self.filter_set = filter_set 
        return filter_set.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre_list'] = Genre.objects.all()
        context['filter'] = self.filter_set
        return context



# def main(request):
#     search = request.GET.get('search')
    
#     if search:
#         movie_list = Movie.objects.filter(name__icontains=search, is_published=True)
#     else:
#         movie_list = Movie.objects.filter(is_published=True)
    
#     genre_list = Genre.objects.all()

#     filter_set = MovieFilter(request.GET, queryset=movie_list)

#     offset = request.GET.get('offset', 1)
#     limit = request.GET.get('limit', 2)

#     paginator = Paginator(filter_set.qs, limit)
#     movie_list = paginator.get_page(offset)

#     return render(request, 'index.html', {
#         'movie_list': movie_list, 
#         'genre_list': genre_list,
#         'filter': filter_set,
#     })


def get_by_genres(request, id):
    # genre = get_object_or_404(Genre, id=id)
    genre_list = Genre.objects.all()
    movie_list = Movie.objects.filter(genres__id=id)
    return render(request, 'index.html', {
        'movie_list': movie_list, 
        'genre_list': genre_list,
    })


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    pk_url_kwarg = 'id'


def movie_detail(request, id):
    # movie = Movie.objects.get(id=id)
    movie = get_object_or_404(Movie, id=id)
    return render(request, 'movie_detail.html', {'movie': movie})



