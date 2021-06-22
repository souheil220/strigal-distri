
from distributeur.models import Commande, Article
import json
import requests
from django.db.models import Q
import base64
from django.conf import settings
from os import walk

# bring pic that i dont have


def schedule_api():
    getAndInsertPhoto()


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
