from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
import json
import requests
from django.http import Http404, HttpResponse
# Create your views here.


def loadMore(request, name):
    if request.is_ajax and request.method == "GET":
        result = Article.objects.filter(nom_article__contains=name)[:5]
        data = {}
        i = 0
        for product in result:
            data[i] = {}
            data[i]['id_article'] = product.id_article
            data[i]['nom_article'] = product.nom_article
            data[i]['unite_mesure'] = product.unite_mesure
            i = i+1

        return HttpResponse(json.dumps(data, indent=4, default=str), content_type="application/json")
    else:
        raise Http404


def list_article():
    try:
        article = Article.objects.all().values_list('product_id')

        if not article:
            print('lol')
            data = []
            pload = {'data': {}}
            print(pload)
            eleme = requests.post(
                "http://10.10.10.64:8585/diststru/prod/", json=pload).json()

            for key in eleme.keys():
                id_article = eleme[key][0]
                nom_article = eleme[key][1]
                type_de_categorie = eleme[key][2]
                categorie_interne = eleme[key][3]
                famille_article = eleme[key][4]
                unite_mesure = eleme[key][5]
                sale_ok = eleme[key][6]
                type_article = eleme[key][7]
                template_id = eleme[key][8]
                company_id = eleme[key][9]
                active = eleme[key][10]
                product_id = eleme[key][11]

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

        else:
            data2 = {}
            i = 0
            for ids in article:
                print(ids[0])
                data2[i] = ids[0]
                i = i + 1
            data = {"data": data2
                    }
            eleme = requests.post(
                "http://10.10.10.64:8585/diststru/prod/", json=data).json()

    except:
        print('error')


def regCommand(request):
    if request.method == "POST":
        try:
            nbr_facture = Distributeur.objects().last().values_list('nbr_facture', flat=True)
        except:
            nbr_facture = 0
        ditributeur = Distributeur(nom='xxx',
                                   adress='xxx',
                                   tel='xxx',
                                   rcn='xxx',
                                   ifn='xxx',
                                   nbr_facture=nbr_facture+1)
        ditributeur.save()

        print(zero_filled_number)

        reference_description = 'DC03' + \
            str(nbr_facture).zfill(4) + "/" + datetime.now().strftime("%y")
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
    # list_article()
    # elem = list_article()
    return render(
        request, "distributeur/commande.html", {
            # "elem": elem
        })


def listCommandes(request):
    return render(
        request, "distributeur/listCommandes.html", {

        })


def index(request):
    return render(
        request, "distributeur/index.html", {

        })
