import django_filters
from django import forms
 
from cinema.models import *


class MovieFilter(django_filters.FilterSet):
    genres = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all(), 
                                                      widget=forms.CheckboxSelectMultiple)
    director = django_filters.ModelChoiceFilter(queryset=Directer.objects.all(), empty_label='choose',
                                                widget=forms.Select)

    class Meta:
        model = Movie
        fields = (
            'genres',
            'director',
            'is_published',
        )
    

