from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from datetime import datetime
import json

import requests
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


def loadMore(request, name, whiche):
    if request.is_ajax and request.method == "GET":
        if(whiche == "1"):
            result = Article.objects.filter(nom_article__contains=name)[:5]
        else:
            result = Article.objects.filter(id_article__contains=name)[:5]

        print(result)
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


# def list_article():
#     try:
#         article = Article.objects.all().values_list('product_id')

#         if not article:
#             print('lol')
#             data = []
#             pload = {'data': {}}
#             print(pload)
#             eleme = requests.post(
#                 "http://10.10.10.64:8585/diststru/prod/", json=pload).json()

#             for key in eleme.keys():
#                 id_article = eleme[key][0]
#                 nom_article = eleme[key][1]
#                 type_de_categorie = eleme[key][2]
#                 categorie_interne = eleme[key][3]
#                 famille_article = eleme[key][4]
#                 unite_mesure = eleme[key][5]
#                 sale_ok = eleme[key][6]
#                 type_article = eleme[key][7]
#                 template_id = eleme[key][8]
#                 company_id = eleme[key][9]
#                 active = eleme[key][10]
#                 product_id = eleme[key][11]

#                 article = Article(id_article=id_article,
#                                   nom_article=nom_article,
#                                   type_de_categorie=type_de_categorie,
#                                   categorie_interne=categorie_interne,
#                                   famille_article=famille_article,
#                                   unite_mesure=unite_mesure,
#                                   sale_ok=sale_ok,
#                                   type_article=type_article,
#                                   template_id=template_id,
#                                   company_id=company_id,
#                                   active=active,
#                                   product_id=product_id
#                                   )
#                 article.save()

#         else:
#             data2 = {}
#             i = 0
#             for ids in article:
#                 print(ids[0])
#                 data2[i] = ids[0]
#                 i = i + 1
#             data = {"data": data2
#                     }
#             eleme = requests.post(
#                 "http://10.10.10.64:8585/diststru/prod/", json=data).json()

#     except:
#         print('error')


def list_destri():
    try:

        print('lol')
        data = []
        pload = {'data': {}}
        print(pload)
        eleme = requests.post(
            "http://10.10.10.64:8585/diststru/", json=pload).json()
        s = "_"
        for key in eleme.keys():
            try:
                x = eleme[key][7].split('@')
                s = x[0]
            except:
                x = eleme[key][3].split()
                if '-' in x[0]:
                    x[0] = x[0].replace('-', '_')
                s = "_"
                s = s.join(x)

            print(s)

            utilisateur = User.objects.create_user(s, None, 'Azerty@22')

            user = utilisateur
            nom = eleme[key][3]
            adress = eleme[key][4]
            tel_fix = eleme[key][5]
            tel_portable = eleme[key][6]
            couriel = eleme[key][7]
            civilite = eleme[key][8]
            site_web = eleme[key][9]
            rcn = eleme[key][10]
            date_enregistrement_rc = eleme[key][11]
            nis = eleme[key][12]
            ifn = eleme[key][13]
            art = eleme[key][14]
            status = eleme[key][16]

            distributeur = Distributeur(user=user,
                                        nom=nom,
                                        adress=adress,
                                        tel_fix=tel_fix,
                                        tel_portable=tel_portable,
                                        couriel=couriel,
                                        civilite=civilite,
                                        site_web=site_web,
                                        rcn=rcn,
                                        date_enregistrement_rc=date_enregistrement_rc,
                                        nis=nis,
                                        ifn=ifn,
                                        art=art,
                                        status=status
                                        )
            distributeur.save()

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
    # list_destri()
    return render(
        request, "distributeur/commande.html", {
            # "elem": elem
        })


@ login_required(login_url='login')
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


def numberToLetter():
    muz = (' ', 'ONZE', 'DOUZE', 'TREIZE',
           'QUATORZE', 'QUINZE', 'SEIZE', 'DIX-SEPT', 'DIX-HUIT', 'DIX-NEUF')

    to_19_fr = ('ZÉRO',  'UN',   'DEUX',  'TROIS', 'QUATRE',   'CINQ',   'SIX',
                'SEPT', 'HUIT', 'NEUF', 'DIX',   'ONZE', 'DOUZE', 'TREIZE',
                'QUATORZE', 'QUINZE', 'SEIZE', 'DIX-SEPT', 'DIX-HUIT', 'DIX-NEUF')
    tens_fr = ('VINGT', 'TRENTE', 'QUARANTE', 'CINQUANTE', 'SOIXANTE',
               'SOIXANTE-DIX', 'QUATRE-VINGT', 'QUATRE-VINGT DIX')
    denom_fr = ('',
                'MILLE',     'MILLION(S)',         'MILLIARDS',       'BILLIONS',       'QUADRILLIONS',
                'QUINTILLION',  'SEXTILLION',      'SEPTILLION',    'OCTILLION',      'NONILLION',
                'DÉCILLION',    'UNDECILLION',     'DUODECILLION',  'TREDECILLION',   'QUATTUORDECILLION',
                'SEXDECILLION', 'SEPTENDECILLION', 'OCTODECILLION', 'ICOSILLION', 'VIGINTILLION')

    def _convert_nn_fr(val):
        """ convertion des valeurs < 100 en Français
        """
        if val < 20:
            return to_19_fr[val]
        for (dcap, dval) in ((k, 20 + (10 * v)) for (v, k) in enumerate(tens_fr)):
            if dval + 10 > val:
                if val % 10:
                    if(val > 70 and val <= 79):
                        dcap = 'SOIXANTE'
                        return dcap + '-' + muz[val % 10]

                    if(val > 90 and val <= 99):
                        dcap = 'QUATRE-VINGT'
                        return dcap + '-' + muz[val % 10]
                    else:
                        return dcap + '-' + to_19_fr[val % 10]

                return dcap

    def _convert_nnn_fr(val):
        """ convert a value < 1000 to french

            special cased because it is the level that kicks 
            off the < 100 special case.  The rest are more general.  This also allows you to
            get strings in the form of 'forty-five hundred' if called directly.
        """
        word = ''
        (mod, rem) = (val % 100, val // 100)
        b = val // 100
        if rem > 0:
            if b == 1:
                word = 'CENT'
            else:
                word = to_19_fr[rem] + ' CENT'
        if mod > 0:
            word += ' '
        if mod > 0:
            word += _convert_nn_fr(mod)
        return word

    def french_number(val):
        if val < 100:
            return _convert_nn_fr(val)
        if val < 1000:
            return _convert_nnn_fr(val)
        for (didx, dval) in ((v - 1, 1000 ** v) for v in range(len(denom_fr))):
            if dval > val:
                mod = 1000 ** didx
                l = val // mod
                r = val - (l * mod)
                if (l == 1) and (denom_fr[didx] == 'MILLE'):
                    ret = denom_fr[didx]
                else:
                    ret = _convert_nnn_fr(l) + ' ' + denom_fr[didx]
                if r > 0:
                    ret = ret + ' ' + french_number(r)
                return ret

    def amount_to_text_fr(number):
        import math
        number = '%.2f' % number

        units_name = ''
        list = str(number).split('.')
        end_word = ''
        muzamil = (french_number(abs(int(list[0]))))
        start_word = muzamil
        final_result = start_word+" DINARS ALGÉRIENS"

        if(len(list) > 1):
            muzamil2 = (french_number(abs(int(list[1]))))
            end_word = muzamil2
            final_result = final_result + " ET "+end_word+" CENTS"
            print(final_result)
        else:
            return french_number + " ET "+"ZERO"+" CENTS"

        # french_number(int(list[1]))
        # cents_number = int(list[1])

        # cents_name = (cents_number > 1) and 'Francs' or 'Franc'
        # final_result = start_word +units_name+' '+ end_word +cents_name
        # return final_result

    print(amount_to_text_fr(426753.00))


def render_to_pdf(request):
    return redirect("https://invoice.strugal-dz.com/stru-invoice-api/PDF/DownloadInvoice?name=DEVIS_STRUGAL_DC_22_01159-22")
