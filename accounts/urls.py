from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_profile, name='login'),
    path('logout/', views.logout_profile, name='logout'),
    path('register/', views.register_profile, name='register'),
]
