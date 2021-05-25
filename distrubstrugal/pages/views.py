from django.shortcuts import render, redirect
from django.contrib.auth.models import  Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
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


def list_destri():
    try:

        print('lol')
        data = []
        pload = {'data': {}}
        print(pload)
        eleme = requests.post(
            "http://10.10.10.64:8585/diststru/", json=pload).json()

        for key in eleme.keys():
            x = eleme[key][7].split('@')
            print(x)
            # User.objects.create_user()

            # user = eleme[key][0]
            # id = eleme[key][1]
            # nom = eleme[key][2]
            # adress = eleme[key][3]
            # tel_fix = eleme[key][4]
            # tel_portable = eleme[key][5]
            # couriel = eleme[key][6]
            # civilite = eleme[key][7]
            # site_web = eleme[key][8]
            # rcn = eleme[key][9]
            # date_enregistrement_rc = eleme[key][10]
            # nis = eleme[key][11]
            # ifn = eleme[key][11]
            # art = eleme[key][11]
            # date_debut_activité = eleme[key][11]
            # date_effet = eleme[key][11]
            # date_echeance = eleme[key][11]
            # status = eleme[key][11]
            # nbr_facture = eleme[key][11]

            # article = Article(id_article=id_article,
            #                   nom_article=nom_article,
            #                   type_de_categorie=type_de_categorie,
            #                   categorie_interne=categorie_interne,
            #                   famille_article=famille_article,
            #                   unite_mesure=unite_mesure,
            #                   sale_ok=sale_ok,
            #                   type_article=type_article,
            #                   template_id=template_id,
            #                   company_id=company_id,
            #                   active=active,
            #                   product_id=product_id
            #                   )
            # article.save()

    except:
        print('error')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        pass_django = 'Azerty@22'
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
                    messages.error(request, 'username or password is invalid')
    return render(request, 'pages/login.html')
