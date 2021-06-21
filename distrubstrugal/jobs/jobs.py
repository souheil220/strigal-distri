
from distributeur.models import Commande, Article
import json
import requests
from django.db.models import Q

# to bring ids of bon de commande from odoo


def schedule_api():
    try:
        commande = Commande.objects.filter(
            n_commande_odoo=None).values('reference_description')
        data2 = {}
        i = 0
        for ids in commande:
            print(ids['reference_description'])
            data2[i] = ids['reference_description']
            i = i + 1
        data = {"data": data2
                }

        eleme = requests.post(
            "http://10.10.10.64:8180/diststru/nodoo/", json=data).json()
        print(eleme)
        if eleme is not None:
            for key in eleme.keys():
                la_commande = Commande.objects.get(
                    reference_description=eleme[key][3])
                la_commande.n_commande_odoo = eleme[key][2]
                la_commande.etat = eleme[key][4]
                if la_commande.etat == 'draft':
                    la_commande.etat = 'Brouillon'
                elif la_commande.etat == 'progress':
                    la_commande.etat = 'En cours'
                elif la_commande.etat == 'confirmed':
                    la_commande.etat = 'confirmé'
                elif la_commande.etat == 'done':
                    la_commande.etat = 'Terminé'
                else:
                    la_commande.etat = 'Annuler'
                la_commande.save()

            print('success')
    except Exception as e:
        print(e)
        print('Error bringing n° odoo')

# to bring new products from odoo


def schedule_api2():
    try:
        article = Article.objects.all().values_list('product_id')
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
            prix_unitaire = eleme[key][17]

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
                              product_id=product_id,
                              prix_unitaire=prix_unitaire)
            article.save()
    except Exception as e:
        print(e)
        print('Error with bringing new articles')


def schedule_api3():
    try:
        commande = Commande.objects.filter(
            ~Q(n_commande_odoo=None), ~Q(etat='done')).values('reference_description', 'etat')
        print(commande)
        data2 = {}
        i = 0
        for ids in commande:
            print(ids['reference_description'])
            data2[i] = ids['reference_description']
            i = i + 1
        data = {"data": {"state": commande[0]['etat'], "n_odoo": data2}
                }

        eleme = requests.post(
            "http://10.10.10.64:8585/diststru/state/", json=data).json()
        if eleme is not None:
            for key in eleme.keys():
                la_commande = Commande.objects.get(
                    reference_description=eleme[key][0])
                la_commande.etat = eleme[key][1]
                la_commande.save()
            print('success')
    except Exception as e:
        print(e)
        print('Error bringing Etat')
