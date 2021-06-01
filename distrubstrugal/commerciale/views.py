from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
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


def annulerCommande(request, id):
    commande = Commande.objects.get(id=id)
    commande.etat = 'Annuler'
    commande.save()
    return redirect('listCommandes')


def ajouterDis(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        adress = request.POST['adress']
        tel_fix = request.POST['tel_fix']
        tel_portable = request.POST['tel_portable']
        couriel = request.POST['couriel']
        civilite = request.POST['civilite']
        site_web = request.POST['site_web']
        rcn = request.POST['rcn']
        date_enregistrement_rc = request.POST['date_enregistrement_rc']
        nis = request.POST['nis']
        ifn = request.POST['ifn']
        art = request.POST['art']
        date_debut_activité = request.POST['date_debut_activité']
        date_effet = request.POST['date_effet']
        date_echeance = request.POST['date_echeance']
        status = request.POST['status']
        s = "_"
        try:
            x = couriel.split('@')
            s = x[0]
        except:
            x = nom.split()
            if '-' in x[0]:
                x[0] = x[0].replace('-', '_')
            s = "_"
            s = s.join(x)
        utilisateur = User.objects.create_user(s, None, 'Azerty@22')
        user = utilisateur
        group = Group.objects.get(name='distributeur')
        user.groups.add(group)
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
                                    date_debut_activité=date_debut_activité,
                                    date_effet=date_effet,
                                    date_echeance=date_echeance,
                                    status=status
                                    )
        distributeur.save()
        return redirect('listCommandes')
    return render(request, 'commerciale/ajouter_dis.html')


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
        return render(request, 'commerciale/renouveler_contrat.html')


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


def suiviContrat(request):
    distributeur = Distributeur.objects.all().values(
        'nom', 'date_effet', 'date_echeance')
    print(distributeur)
    context = {
        'distributeur': distributeur
    }
    return render(request, 'commerciale/suivi_contrat.html', context)


def filterer(request, dist=None, date=None):
    if request.is_ajax and request.method == "GET":
        print(date == 'None')
        if date == 'None':
            print('rani fel if')
            distributeur = Distributeur.objects.filter(nom=dist).values(
                'id', 'nom', 'date_effet', 'date_echeance')
            print(distributeur)
            return HttpResponse(json.dumps(distributeur[0], indent=4, default=str), content_type="application/json")
        else:
            print('rani fel else')
            distributeur = Distributeur.objects.filter(date_echeance=date).values(
                'nom', 'date_effet', 'date_echeance')
            print(distributeur)
            return HttpResponse(json.dumps(distributeur[0], indent=4, default=str), content_type="application/json")


def renouveler_contrat(request):
    return render(request, "commerciale/renouveler_contrat.html")
