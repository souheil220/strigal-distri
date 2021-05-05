from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .sql import connexion_ad2000, connexion_email
import re


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


def test(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        pass_django = 'Azerty@22'
        if not re.match(r"^[A-Za-z0-9\.\+-]+@[A-Za-z0-9\.-]+\.[a-zA-Z]*$", username):
            email_util = 'GROUPE-HASNAOUI\\' + username
            connexion = connexion_ad2000(email_util, password)
        else:
            connexion = connexion_email(username, password)
        if connexion == 'deco':
            return render(request, 'pages/login.html', {'msg': 'Accès non autorisé'})
        else:
            print(connexion['ad_2000'])
            user = authenticate(
                request, username=connexion['ad_2000'], password=pass_django)
            if user is not None:
                login(request, user)
                return redirect("index")
                # return affectation_societe(int(request.user.first_name))
            else:
                messages.info(request, 'username or password is invalid')
    return render(request, 'pages/login.html')
