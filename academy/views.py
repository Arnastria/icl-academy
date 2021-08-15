from django.http.response import HttpResponseBadRequest
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def form_registration(request):
    print(request.POST)
    return render(request, 'form_registration.html')


def login_me(request):
    if(request.POST == {}):
        print("GET")
        return render(request, 'login.html')
    else:
        print("POST")
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if(user.user_level == 0):
                return redirect('/dashboard/')
            return redirect('/')
        else:
            return render(request, 'login.html', {'message': 'wrong username or password'})


def logout_me(request):
    logout(request)
    return redirect('/')


def register_class(request):
    if(request.GET == {}):
        return render(request, 'register_class.html')
    else:
        print(request.GET)
        return render(request, 'register_class.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def landing(request):
    return render(request, 'landing.html')
