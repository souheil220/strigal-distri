from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
import psycopg2
import json
import requests
import pandas as pd
# Create your views here.


def getProduct(request):
    pass


def list_article():
    try:
        article = Article.objects.all()
    except:
        data = []

        eleme = requests.post(
            "http://10.10.10.64:8585/diststru/prod/", data='pload').json()

        for key in eleme.keys():
            data.append(eleme[key])
            id_article = data[0]
            nom_article = data[1]
            type_de_categorie = data[2]
            categorie_interne = data[3]
            famille_article = data[4]
            unite_mesure = data[5]
            sale_ok = data[6]
            type_article = data[7]
            template_id = data[8]
            company_id = data[9]
            active = data[10]
            product_id = data[11]

            article = Article(id_article=id_article,
                              nom_article=nom_article,
                              type_de_categorie=type_de_categorie,
                              categorie_interne=categorie_interne,
                              famille_article=famille_article,
                              unite_mesure=unite_mesure,
                              sale_ok=sale_ok,
                              type_article=type_article,
                              template_id=template_id,
                              company_id=company_id,
                              active=active,
                              product_id=product_id
                              )
            article.save()

        print(data)
        # print(data)
        return data


def regCommand(request):
    if request.method == "POST":
        try:
            nbr_facture = Distributeur.objects().last().values_list('nbr_facture', flat=True)
        except:
            nbr_facture = 1
        ditributeur = Distributeur(nom='xxx',
                                   adress='xxx',
                                   tel='xxx',
                                   rcn='xxx',
                                   ifn='xxx',
                                   nbr_facture=nbr_facture+1)
        ditributeur.save()

        print(zero_filled_number)

        reference_description = 'DC03' + \
            str(nbr_facture).zfill(4) + datetime.now().strftime("%y")
        commande = Commande(reference_description=reference_description,
                            destributeur=User,
                            societe='strugal',
                            totaleHT=request.POST['MHT'],
                            totaleTTC=request.POST['TTC'],
                            )
        commande.save()

        request.POST['datalength']
        for i in range(1, int(datalength) + 1):
            id_commande = Commande.objects().last().values_list('id', flat=True),
            code_article = '',
            description = request.POST['description-{}'.format(i)],
            qte = request.POST['quantite-{}'.format(i)],
            montant = request.POST['mantant-{}'.format(i)],

            list_article_commande = ListArticleCommande(id_commande=id_commande,
                                                        code_article=code_article,
                                                        description=description,
                                                        qte=int(qte),
                                                        montant=montant,)

            list_article_commande.save()

            return redirect('/distributeur/listCommandesD/')


def commande(request):
    elem = list_article()
    return render(
        request, "distributeur/commande.html", {
            "elem": elem
        })


def listCommandes(request):
    return render(
        request, "distributeur/listCommandes.html", {

        })


def index(request):
    return render(
        request, "distributeur/index.html", {

        })
