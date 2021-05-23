from django.shortcuts import render
from distributeur.models import Commande, ListArticleCommande, Distributeur
import json
from django.http import Http404, HttpResponse
# Create your views here.


def listCommandes(request):

    commande = Commande.objects.all()
    context = {
        "commande": commande
    }

    return render(
        request, "commerciale/listCommandes.html", context)


def detailCommande(request, id):
    if request.is_ajax and request.method == "GET":
        list_commande = ListArticleCommande.objects.filter(id_commande=id).values(
            'code_article__id_article',
            'code_article__nom_article',
            'code_article__prix_unitaire',
            'qte',
            'id_commande__totaleTTC',
            'id_commande__date',
            'id_commande__reference_description',
            'id_commande__societe',
            'id_commande__destributeur__nom',
            "code_article__unite_mesure",
            "id_commande__totaleHT",
            "id_commande__n_commande_odoo",
            "montant")
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
        tva = int(list_commande[0]["id_commande__totaleHT"]) * 19 / 100
        return render(request, "commerciale/detail.html", {'list_commande': list_commande,
                                                           'totalTTC': list_commande[0]['id_commande__totaleTTC'],
                                                           "n_commande_odoo": list_commande[0]['id_commande__n_commande_odoo'],
                                                           "societe": list_commande[0]["id_commande__societe"],
                                                           "client": list_commande[0]["id_commande__destributeur__nom"],
                                                           "totaleHT": list_commande[0]["id_commande__totaleHT"],
                                                           "tva": tva,
                                                           "date": list_commande[0]["id_commande__date"],
                                                           "reference_description": list_commande[0]["id_commande__reference_description"], })
    else:
        raise Http404


def renew(request):
    if request.method == "POST":
        id = request.POST.get('distributeur')
        new_date = request.POST.get('demo-date')

        distributeur = Distributeur.objects.get(id=int(id))
        print(new_date)
        distributeur.date_echeance = new_date
        distributeur.save()
        return render('commerciale/renouveler_contrat.html')


def loadMore(request, name):
    if request.is_ajax and request.method == "GET":

        result = Distributeur.objects.filter(nom__contains=name)[:5]

        print(result)
        data = {}
        i = 0
        for user in result:
            data[i] = {}
            data[i]['id_ditributeur'] = user.id
            data[i]['nom_ditributeur'] = user.nom
            i = i+1

        return HttpResponse(json.dumps(data, indent=4, default=str), content_type="application/json")

    else:
        raise Http404


def renouveler_contrat(request):
    return render(request, "commerciale/renouveler_contrat.html")
