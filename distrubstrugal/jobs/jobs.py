
from distributeur.models import Commande
import json
import requests


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
        print('error')
