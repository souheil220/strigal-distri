
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
            "http://10.10.10.64:8585/diststru/nodoo/", json=data).json()
        print(eleme)
        if eleme is not None:
            for key in eleme.keys():
                la_commande = Commande.objects.get(
                    reference_description=eleme[key][3])
                la_commande.n_commande_odoo = eleme[key][0]
                la_commande.etat = eleme[key][4]
                la_commande.save()
            print('success')
    except:
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
    except:
        print('Error with bringing new articles')


def schedule_api3():
    try:
        commande = Commande.objects.filter(
            ~Q(n_commande_odoo=None), ~Q(etat='done')).values('reference_description', 'etat')
        last_commande = (Commande.objects.last().reference_description)[-2:]
        print(last_commande)
        # data2 = {}
        # i = 0
        # for ids in commande:
        #     print(ids['reference_description'])
        #     data2[i] = ids['reference_description']
        #     i = i + 1
        # data = {"data": {"state": commande[0]['etat'], "n_odoo": data2}
        #         }

        # eleme = requests.post(
        #     "http://10.10.10.64:8585/diststru/state/", json=data).json()
        # if eleme is not None:
        #     for key in eleme.keys():
        #         la_commande = Commande.objects.get(
        #             reference_description=eleme[key][0])
        #         la_commande.etat = eleme[key][1]
        #         la_commande.save()
        #     print('success')
    except:
        print('Error bringing Etat')
