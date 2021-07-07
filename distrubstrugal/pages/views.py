from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from .sql import connexion_ad2000, connexion_email
from distributeur.models import Distributeur
import re
from datetime import datetime, date


rest = None


def index(request):
    if request.user.is_authenticated:
        # print("user",request.user)
        query_set = Group.objects.filter(user=request.user)
        print(query_set)
        profile = ""
        for g in query_set:
            profile = g
        print(profile.name)
        if profile.name == 'commercial' or profile.name == "super_commercial":
            return redirect("commerciale/listCommandesC")
        else:
            rest = calculDate(request.user)
            return render(request, "distributeur/commande.html", {'rest': rest.days})

    return render(request, 'pages/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        if '@' in username:
            try:
                user = User.objects.get(email=username)
            except:
                messages.error(
                    request, 'Utilisateur innexistant')
                return render(request, 'pages/login.html')

        else:
            try:
                user = User.objects.get(username=username)
            except:
                messages.error(
                    request, 'Utilisateur innexistant')
                return render(request, 'pages/login.html')

        query_set = Group.objects.filter(user=user)
        profile = ""
        for g in query_set:
            profile = g
        if profile.name == 'commercial':

            # connexionAd(request, username, password)
            pass_django = 'Azerty@22'
            if not re.match(r"^[A-Za-z0-9\.\+-]+@[A-Za-z0-9\.-]+\.[a-zA-Z]*$", username):
                email_util = 'GROUPE-HASNAOUI\\' + username
                connexion = connexion_ad2000(email_util, password)
            else:
                connexion = connexion_email(username, password)

            print("connexion ", connexion)
            if connexion == 'deco':
                messages.error(request, 'Something went wrong')
            else:
                user = authenticate(
                    request, username=connexion['ad_2000'], password=pass_django)
                print("user", user)

                if user is not None:
                    login(request, user)
                    return redirect("index")

                else:
                    messages.error(request, 'Accès non autorisé')
        else:
            rest = calculDate(user)
            if(rest.days > 0):
                login(request, user)
                return redirect("index")
            else:
                messages.error(
                    request, 'Votre contrat a expiré veuillez le renouveler')

    return render(request, 'pages/login.html')


def calculDate(user):
    distri = Distributeur.objects.get(user=user)
    dateFinC = distri.date_echeance
    today = date.today()
    date_fin_contrat = datetime.strptime(dateFinC, '%Y-%m-%d')
    d1 = today.strftime("%Y-%m-%d")
    date_aujourdui = datetime.strptime(d1, '%Y-%m-%d')
    rest = date_fin_contrat - date_aujourdui
    return rest
