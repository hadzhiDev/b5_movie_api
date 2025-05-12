from django.db import models
from django.db.models import Model


class Directer(Model): 
    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'

    full_name = models.CharField(verbose_name='ФИО', max_length=300)
    image = models.ImageField(verbose_name='изображение', upload_to='directerImages', )
 
    def __str__(self) -> str:
        return self.full_name
    

class Genre(Model):
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    name = models.CharField(verbose_name='название', max_length=300)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    name = models.CharField(verbose_name='название', max_length=300)
    description = models.CharField(verbose_name='описание', max_length=600, null=True, blank=True)
    year = models.IntegerField(verbose_name='год выпуска')
    rating = models.IntegerField(verbose_name='рейтинг')
    duration = models.CharField(verbose_name='продолжительность', max_length=200)
    image = models.ImageField(verbose_name='изображение', upload_to='movieImages', null=True, blank=True)
    director = models.ForeignKey('cinema.Directer', on_delete=models.CASCADE, verbose_name='Режиссер фильма', null=True)
    genres = models.ManyToManyField('cinema.Genre', verbose_name='Жанры', related_name='movies')
    is_published = models.BooleanField(default=True, verbose_name='публичность')
    content = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} - {self.year}'


class Comment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-date',)

    name = models.CharField(verbose_name='Имя', max_length=200)
    text = models.CharField(verbose_name='текст', max_length=400)
    movie = models.ForeignKey('cinema.Movie', on_delete=models.CASCADE, related_name='comments', verbose_name='Фильм')
    date = models.DateTimeField(verbose_name='дата', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.movie.name}'


class Atrubute(models.Model):
    class Meta:
        verbose_name = 'Атрибут'
        verbose_name_plural = 'Атрибуты'

    name = models.CharField(verbose_name='название', max_length=300)
    movie = models.ForeignKey('cinema.Movie', on_delete=models.CASCADE, related_name='attributes', verbose_name='Фильм')
    value = models.CharField(verbose_name='значение', max_length=300)

    def __str__(self):
        return f'{self.name} - {self.movie.name}'