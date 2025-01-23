from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from accounts.managers import UserManager


class User(AbstractUser):
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('-date_joined',)

    username = None
    avatar = ResizedImageField(size=[500, 500], crop=['middle', 'center'], upload_to='avatars/',
                               force_format='WEBP', quality=90, verbose_name='аватарка',
                               null=True, blank=True)
    phone = PhoneNumberField(max_length=100, unique=True, verbose_name='номер телефона', blank=True, null=True)
    email = models.EmailField(verbose_name='электронная почта', unique=True, blank=False, null=False)
    groups = models.ManyToManyField(Group, related_name='account_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='account_users_permissions', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def get_full_name(self):
        return f'{self.last_name} {self.first_name}'

    get_full_name.fget.short_description = 'полное имя'

    def __str__(self):
        return f'{self.get_full_name or str(self.email)}'

