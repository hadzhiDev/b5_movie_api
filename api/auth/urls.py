from django.urls import path
from . import views



urlpatterns = [
    path('login/', views.LoginGenericAPIView.as_view()),
    path('register/', views.RegisterGenericApiView.as_view()),
    path('change-password/', views.ChangePasswordApiView.as_view()),
]