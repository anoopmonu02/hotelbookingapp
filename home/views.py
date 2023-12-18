from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if not user_obj.exists():
            messages.warning(request, 'Username not found.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        #if username exists then-
        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.warning(request, 'Invalid Credential!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        login(request, user_obj)
        return redirect('/')
    return render(request, 'login.html')


def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)

        if user_obj.exists():
            messages.warning(request, 'User already registered.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        #if username not exists then-
        user = User.objects.create(
            username=username)
        user.set_password(password)
        user.save()
        messages.success(request, 'User registered.')
        return redirect('/')

    return render(request, 'register.html')

def logout_page(request):
    return render(request, 'logout.html')