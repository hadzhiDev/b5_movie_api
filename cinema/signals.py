from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
from django.dispatch import receiver

from .models import Movie, Genre, Directer


@receiver(pre_save, sender=Movie)
def movie_pre_create_signal(sender, instance, **kwargs):
    if instance.pk is None:
        print('Signal pre save for a new movie')
    else:
        print('Signal pre save for an existing movie')


@receiver(post_save, sender=Movie)
def movie_create_signal(sender, instance, created, **kwargs):
    if created:
        # print('Signal pre save')
        print(f'The movie {instance.name} was created')


@receiver(post_delete, sender=Movie)
def movie_create_signal(sender, instance, **kwargs):
    print(f'The movie {instance.name} was deleted')


