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
        print(type(profile.name))
        if profile.name == 'commercial':
            return redirect("commerciale/listCommandesC")
        else:
            distri = Distributeur.objects.get(user=request.user)
            dateFinC = distri.date_echeance
            today = date.today()
            date_fin_contrat = datetime.strptime(dateFinC, '%Y-%m-%d')
            d1 = today.strftime("%Y-%m-%d")
            date_aujourdui = datetime.strptime(d1, '%Y-%m-%d')
            rest = date_fin_contrat - date_aujourdui
            print(rest)
            return render(request, "distributeur/commande.html", {'rest': rest.days})

    return render(request, 'pages/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        pass_django = 'Azerty@22'
        if '@' in username:
            try:
                user = authenticate(
                    request, username=User.objects.get(email=username), password=password)
            except:
                user = None
                messages.error(
                    request, 'Utilisateur innexistant')

        else:
            user = authenticate(
                request, username=username, password=password)
        if user is not None:
            print(user)

            distri = Distributeur.objects.get(user=user)
            dateFinC = distri.date_echeance
            today = date.today()
            date_fin_contrat = datetime.strptime(dateFinC, '%Y-%m-%d')
            d1 = today.strftime("%Y-%m-%d")
            date_aujourdui = datetime.strptime(d1, '%Y-%m-%d')
            if(date_aujourdui < date_fin_contrat):
                rest = date_fin_contrat - date_aujourdui
                print(rest.days)
                login(request, user)
                return redirect("index")
            else:
                messages.error(
                    request, 'Votre contrat a expiré veuillez le renouveler')
        else:
            if not re.match(r"^[A-Za-z0-9\.\+-]+@[A-Za-z0-9\.-]+\.[a-zA-Z]*$", username):
                email_util = 'GROUPE-HASNAOUI\\' + username
                connexion = connexion_ad2000(email_util, password)
            else:
                connexion = connexion_email(username, password)
            if connexion == 'deco':
                messages.error(request, 'Accès non autorisé')
                # return render(request, 'pages/login.html', {'msg': ''})
            else:
                print(connexion['ad_2000'])
                user = authenticate(
                    request, username=connexion['ad_2000'], password=pass_django)

                if user is not None:
                    login(request, user)
                    return redirect("index")

                else:
                    try:
                        utilisateur = User.objects.create_user(username, None,
                                                               'Azerty@22')
                        utilisateur.save()
                        group = Group.objects.get(name='commercial')
                        utilisateur.groups.add(group)
                        user = authenticate(request,
                                            username=connexion['ad_2000'],
                                            password=pass_django)
                        login(request, user)
                        return redirect("index")
                    except Exception as e:
                        print(e)

    return render(request, 'pages/login.html')
