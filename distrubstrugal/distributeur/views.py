from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
import psycopg2
import json
import requests
import pandas as pd
# Create your views here.


def list_distrib():
    # eleme = json.loads(requests.post(
    #     "http://10.10.10.64:8585/diststru/").text)
    # print(eleme)
    eleme = (requests.request('POST', "http://10.10.10.64:8585/diststru/"))
    data = []
    for row in eleme:
        print(row)
    # print(data)
    return eleme


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
    print('test')
    print(list_distrib())
    return render(
        request, "distributeur/commande.html", {

        })


def listCommandes(request):
    return render(
        request, "distributeur/listCommandes.html", {

        })


def index(request):
    return render(
        request, "distributeur/index.html", {

        })
