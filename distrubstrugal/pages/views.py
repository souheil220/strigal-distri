from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


def index(request):
    if request.user.is_authenticated:
        # print("user",request.user)
        query_set = Group.objects.filter(user=request.user)
        profile = ""
        for g in query_set:
            profile = g
        print(type(profile.name))
        if profile.name == 'commercial':
            return redirect("commerciale/listCommandesC")
        else:
            return redirect("distributeur/commande")

    return render(request, 'pages/login.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, 'username or password is invalid')

    return render(request, 'pages/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
