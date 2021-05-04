from django.shortcuts import render
from distributeur.models import Commande, ListArticleCommande

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
            'qte',
            'id_commande__totaleTTC',
            'id_commande__date',
            'id_commande__reference_description',
            'id_commande__societe',
            'id_commande__destributeur__nom',
            "code_article__unite_mesure",
            "id_commande__totaleHT",
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
        return render(request, "commerciale/detail.html", {'list_commande': list_commande, 'totalTTC': list_commande[0]['id_commande__totaleTTC'], "societe": list_commande[0]["id_commande__societe"],
                                                           "client": list_commande[0]["id_commande__destributeur__nom"],
                                                           "totaleHT": list_commande[0]["id_commande__totaleHT"],
                                                           "tva": tva,
                                                           "date": list_commande[0]["id_commande__date"],
                                                           "reference_description": list_commande[0]["id_commande__reference_description"], })
    else:
        raise Http404
