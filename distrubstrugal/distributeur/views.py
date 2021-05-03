from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
import json
import requests
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
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
        current_user = request.user
        try:
            nbr_facture = Distributeur.objects.get(
                user=current_user).nbr_facture
            nbr_facture = nbr_facture+1
            Distributeur.objects.filter(user=current_user).update(
                nbr_facture=nbr_facture)
        except:
            nbr_facture = 0
        distributeur = Distributeur.objects.get(
            user=current_user)
        reference_description = 'DC' + (str(current_user.id).zfill(2)) + \
            str(nbr_facture).zfill(4) + "/" + datetime.now().strftime("%y")
        commande = Commande(reference_description=reference_description,
                            destributeur=distributeur,
                            societe='strugal',
                            totaleHT=request.POST.get('MHT'),
                            totaleTTC=request.POST.get('TTC'),
                            )
        commande.save()
        datalength = request.POST['datalength']
        for i in range(1, int(datalength) + 1):
            id_commande = Commande.objects.all().last()
            article = request.POST.get('article-{}'.format(i))
            code_article = Article.objects.get(id_article=article)
            qte = request.POST['quantite-{}'.format(i)]

            montant = request.POST.get('mantant-{}'.format(i))
            print(montant)

            list_article_commande = ListArticleCommande(id_commande=id_commande,
                                                        code_article=code_article,
                                                        qte=int(qte),
                                                        montant=int(montant),)

            list_article_commande.save()

        return redirect('/distributeur/listCommandesD')


@ login_required(login_url='login')
def commande(request):
    # list_article()
    # elem = list_article()
    return render(
        request, "distributeur/commande.html", {
            # "elem": elem
        })


def listCommandes(request):
    current_user = request.user
    destributeur = Distributeur.objects.get(user=current_user)
    commande = Commande.objects.filter(destributeur=destributeur)
    # test = []
    # for i in commande:
    #     print(i.id)
    #     list_commande = ListArticleCommande.objects.filter(id_commande=i.id)
    #     print(list_commande)
    #     test.append(list_commande)
    print(commande)
    context = {
        "commande": commande
    }
    return render(
        request, "distributeur/listCommandes.html", context)


def detailCommande(request, id):
    if request.is_ajax and request.method == "GET":
        list_commande = ListArticleCommande.objects.filter(id_commande=id).values(
            'code_article__id_article', 'code_article__nom_article', 'qte', 'id_commande__totaleTTC')
        print(list_commande[0]['id_commande__totaleTTC'])
        # data = {}
        # i = 0
        # for p in list_commande:

        #     print(p.code_article.nom_article)
        #     data[i]['id_article'] = p.code_article.id_article
        #     data[i]['nom_article'] = p.code_article.nom_article
        #     data[i]['qte'] = p.qte
        # return HttpResponse(json.dumps(data, indent=4, default=str), content_type="application/json")
        # return HttpResponse(list_commande)
        return render(request, "distributeur/detail.html", {'list_commande': list_commande, 'totalTTC': list_commande[0]['id_commande__totaleTTC']})
    else:
        raise Http404
