from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from cinema.models import Movie, Directer, Genre, Comment


class MovieAdminForm(forms.ModelForm):

    content = forms.CharField(widget=CKEditorUploadingWidget(), label='Контент')

    class Meta:
        model = Movie 
        fields = '__all__'


class CommentStackedinline(admin.StackedInline):
    extra = 1
    model = Comment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'rating')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'year')
    list_filter = ('year', 'genres')
    filter_horizontal = ('genres',)
    form = MovieAdminForm
    inlines = (CommentStackedinline,)


@admin.register(Directer)
class DirecterAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')
    search_fields = ('id', 'full_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'movie__name', 'date')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'movie__name',)


# admin.site.register(Movie)
# admin.site.register(Directer)
# admin.site.register(Genre)
