
from distributeur.models import Commande, Article
import json
import requests
from django.db.models import Q
import base64
from django.conf import settings
from os import walk
import psycopg2

# bring pic that i dont have


def schedule_api():
    getAndInsertPhoto()

# bring N_odoo


def schedule_api2():
    # bring N_odoo
    try:
        commande = Commande.objects.filter(
            n_commande_odoo=None).values('reference_description')
        data2 = {}
        i = 0
        if len(commande) > 0:
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
                    la_commande.etat = "En cours"
                    la_commande.save()

                print('success')
    except Exception as e:
        print(e)
        print('Error bringing n° odoo')

# bring Etat


def schedule_api3():

    try:

        commande = Commande.objects.exclude(etat__in=[
            "Annulé", 'Livré']).exclude(n_commande_odoo=None).values('reference_description', 'etat')
        data2 = {}
        i = 0
        if len(commande) > 0:
            for ids in commande:
                data2[i] = ids['reference_description']
                i = i + 1
            data = {"data": {"state": commande[0]['etat'], "n_odoo": data2}
                    }

            eleme = requests.post(
                "http://10.10.10.64:8180/diststru/state/", json=data).json()
            if eleme is not None:
                for key in eleme.keys():
                    la_commande = Commande.objects.get(
                        reference_description=eleme[key][0])

                    if eleme[key][1] == 'drafte':
                        la_commande.etat = 'Brouillon'
                    elif eleme[key][1] == 'progress':
                        la_commande.etat = 'En cours'
                    elif eleme[key][1] == 'confirmed':
                        la_commande.etat = 'confirmé'
                    elif eleme[key][1] == 'done':
                        la_commande.etat = 'Terminé'
                    else:
                        la_commande.etat = 'Annulé'
                    la_commande.save()
                print('success')
    except Exception as e:
        print(e)
        print('Error bringing Etat')


def GetFromOdoo(query):
    try:
        print("Getting Data from Odoo ...")
        with psycopg2.connect(host='10.20.10.43', user='hasnaoui_bi', password='Cbi@venger$2020',
                              dbname='hasnaoui') as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            cursor.close()
        print("Data downloaded from Odoo server ...")
        connection.close()
        if data:
            return {"retrieve": True, "data": data}
        else:
            return {"retrieve": False, "exception": "Empty list"}
    except Exception as error:
        return {"retrieve": False, "exception": str(error)}


def getAndInsertPhoto():
    image_path = settings.MEDIA_ROOT + '/photo_produit'

    filenames = next(walk(image_path), (None, None, []))[2]

    exlure = ""
    for nom in filenames:
        exlure = exlure + "'" + nom[:-4]+"'" + ","
    l = len(exlure)
    exlure = exlure[:l-1]

    query = """select
                            p.default_code
                            ,tp.image_small
                            from product_product p,res_company r,product_uom u,product_template tp
                            left join product_template_company_allowed_rel c On tp.id=c.template_id
                            left join res_company rr on rr.id=c.company_id
                            left join product_category pc on tp.categ_id=pc.id
                            left join product_category as pc1 on pc1.id=pc.parent_id
                            left join product_category as pc2 on pc2.id=pc1.parent_id
                            left join product_category as pc3 on pc3.id=pc2.parent_id
                            left join product_category as pc4 on pc4.id=pc3.parent_id
                            left join product_category as pc5 on pc5.id=pc4.parent_id
                            left join product_category as pc6 on pc5.id=pc6.parent_id
                            where tp.image_small notnull 
                                    and  (p.product_tmpl_id=tp.id)
                                    and (r.id=tp.company_id)
                                    and(tp.uom_id=u.id) and tp.sale_ok=true and tp.company_id=19 and tp.active=true
                                    and p.default_code not in ("""+exlure+""")
                                order by p.create_date desc"""

    photos = GetFromOdoo(query=query)

    if not photos["retrieve"]:
        return {"synchronized": False, "exception": photos["exception"]}
    else:
        photos = photos["data"]
        for photo in photos:
            image = memoryview.tobytes(photo[1])
            open(f"{image_path}/{photo[0]}.png",
                 "wb").write(base64.decodebytes(image))
