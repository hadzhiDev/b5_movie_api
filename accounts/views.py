from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

from accounts.models import User


@csrf_exempt
def register_profile(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not email or not password or not confirm_password:
            return render(request, 'auth/register.html', {'message': 'Enter required fields'})
        
        if password != confirm_password:
            return render(request, 'auth/register.html', {'message': 'Passwords do not match'})

        if User.objects.filter(email=email).exists():
            return render(request, 'auth/register.html', {'message': 'User with this email already exists'})
        
        user = User.objects.create_user(email=email, password=password)
    
        login(request, user)
        return redirect('/')
    
    return render(request, 'auth/register.html')



@csrf_exempt
def login_profile(request):

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email == '' or password == '':
            return render(request, 'auth/login.html', {'message': 'Enter required fields'})
        
        user = authenticate(email=email, password=password)

        if user:
            login(request, user)
            return redirect('/')
        
        return render(request, 'auth/login.html', {'message': 'The user is not found or invalid password'})
    
    return render(request, 'auth/login.html')


def logout_profile(request):
    if request.user.is_authenticated:
        logout(request) 
    return redirect('/')