from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from distributeur.models import Commande, ListArticleCommande, Distributeur, Article
import json
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.files.storage import FileSystemStorage
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


def detailAndModif(id):
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
    tva = int(list_commande[0]["id_commande__totaleHT"]) * 19 / 100
    context = {"id": id,
               'list_commande': list_commande,
               'totalTTC': list_commande[0]['id_commande__totaleTTC'],
               "n_commande_odoo": list_commande[0]['id_commande__n_commande_odoo'],
               "societe": list_commande[0]["id_commande__societe"],
               "client": list_commande[0]["id_commande__destributeur__nom"],
               "totaleHT": list_commande[0]["id_commande__totaleHT"],
               "tva": tva,
               'montant': list_commande[0]["montant"],
               "date": list_commande[0]["id_commande__date"],
               "reference_description": list_commande[0]["id_commande__reference_description"], }

    return context


def detailCommande(request, id):
    if request.is_ajax and request.method == "GET":
        context = detailAndModif(id)
        print(context)
        return render(request, "commerciale/detail.html", context)
    else:
        raise Http404


def modifierCommande(request, id):
    if request.method == "POST":
        datalength = request.POST['datalength']
        commande = Commande.objects.get(id=int(id))
        commande.totaleHT = request.POST.get('MHT')
        commande.totaleTTC = request.POST.get('TTC')
        upload_file = request.FILES['capture']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        url = fs.url(name)
        commande.capture = url
        commande.save()
        for i in range(1, int(datalength) + 1):
            list_article_commande = ListArticleCommande.objects.filter(
                id_commande=commande)[i-1]
            article = request.POST.get('code_article-{}'.format(i))
            print(article)
            list_article_commande.code_article = Article.objects.get(
                id_article=article)
            list_article_commande.qte = request.POST['quantite-{}'.format(i)]
            list_article_commande.prix_unitaire = request.POST.get(
                'prix_unitaire-{}'.format(i))
            list_article_commande.montant = request.POST.get(
                'mantant-{}'.format(i))

            list_article_commande.save()

        return redirect("listCommandes")
    elif request.is_ajax and request.method == "GET":
        context = detailAndModif(id)
        print((context))
        print(len(context['list_commande']))
        return render(request, "commerciale/modifier.html", context)
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


def loadMoreD(request, argum, whicheone):
    if request.is_ajax and request.method == "GET":
        if (whicheone == 'dist'):
            result = Distributeur.objects.filter(nom__contains=argum)[:5]

            print(result)
            data = {}
            i = 0
            for user in result:
                data[i] = {}
                data[i]['id_ditributeur'] = user.id
                data[i]['nom_ditributeur'] = user.nom
                i = i+1

        else:
            result = Commande.objects.filter(
                reference_description__contains=argum)[:5]

            print(result)
            data = {}
            i = 0
            for commande in result:
                data[i] = {}
                data[i]['id_commande'] = commande.id
                data[i]['reference_description'] = commande.reference_description
                i = i+1

        return HttpResponse(json.dumps(data, indent=4, default=str), content_type="application/json")

    else:
        raise Http404


def detailDisti(request, id):
    if request.is_ajax and request.method == "GET":
        distributeur = Distributeur.objects.get(id=id)
        context = {"nom": distributeur.nom,
                   "adress": distributeur.adress,
                   "tel_portable": distributeur.tel_portable,
                   "couriel": distributeur.couriel,
                   "date_effet": distributeur.date_effet,
                   "date_echeance": distributeur.date_echeance,
                   "nbr_facture": distributeur.nbr_facture, }
        return render(request, "commerciale/detailD.html", context)
    else:
        raise Http404


def suiviContrat(request):
    distributeur = Distributeur.objects.all()[:5].values(
        'id', 'nom', 'date_effet', 'date_echeance')
    print(distributeur)
    context = {
        'distributeur': distributeur
    }
    return render(request, 'commerciale/suivi_contrat.html', context)


def get_filter_data(distributeur):
    i = 0
    final_data = {}
    for dist in distributeur:
        final_data[i] = {}
        final_data[i]['id'] = dist['id']
        final_data[i]['nom'] = dist['nom']
        final_data[i]['date_effet'] = dist['date_effet']
        final_data[i]['date_echeance'] = dist['date_echeance']
        i += 1
    return final_data


def filterer(request, dist=None, date=None):
    if request.is_ajax and request.method == "GET":
        if date == 'None':
            distributeur = Distributeur.objects.filter(nom=dist).values(
                'id', 'nom', 'date_effet', 'date_echeance')
            print(distributeur[0]['id'])

            return HttpResponse(json.dumps(distributeur[0], indent=4, default=str), content_type="application/json")
        else:
            if dist == 'None':
                distributeur = Distributeur.objects.filter(date_echeance=date).values(
                    'id', 'nom', 'date_effet', 'date_echeance')
            else:
                distributeur = Distributeur.objects.filter(date_echeance=date, nom=dist).values(
                    'id', 'nom', 'date_effet', 'date_echeance')
            final_data = get_filter_data(distributeur)
            print('final_data ', final_data)

            context = {"result": final_data}
            return HttpResponse(json.dumps(context, indent=4, default=str), content_type="application/json")


def search(**kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v != 'None'}
    print("kwargs ", kwargs)
    queryset = Commande.objects.filter(**kwargs)
    print('query :', queryset)
    return queryset


def filtererListCommand(request, dist, date, etat, refdes):

    print("refdes : ", refdes == 'Recherche par Ref Des')
    if request.is_ajax and request.method == 'GET':
        print(dist == 'Recherche Ditributeur')
        if dist != 'None' and dist != 'Recherche Ditributeur':
            dist = Distributeur.objects.filter(nom=dist)[0]
        else:
            dist = 'None'

        if refdes != 'None' and refdes != 'Recherche par Ref Des':
            refdes = refdes.replace('-', '/')
        else:
            refdes = 'None'
        print("refdes : ", refdes)
        data = search(date=date, destributeur=dist,
                      etat=etat, reference_description=refdes)
        print("data : ", data)
        i = 0
        final_data = {}
        for d in data:
            final_data[i] = {}
            final_data[i]['id'] = d.id
            final_data[i]['date'] = d.date
            final_data[i]['n_commande_odoo'] = d.n_commande_odoo
            final_data[i]['destributeur'] = d.destributeur.nom
            final_data[i]['reference_description'] = d.reference_description
            final_data[i]['totaleHT'] = d.totaleHT
            final_data[i]['totaleTTC'] = d.totaleTTC
            final_data[i]['etat'] = d.etat
            i += 1
        # option = {}
        # if etat != 'None':
        #     result = Commande.objects.filter(date=date,etat=etat)
        # if refdes != 'None':
        #     result = Commande.objects.filter(date=date,etat=etat,reference_description=refdes)
        # if dist != 'None':
        #     distributeur = Distributeur.objects.filter(nom=dist)
        #     option['dist'] = distributeur
        # if option != {}:
        #     print(("%s" %option).replace("{","").replace("}","").replace(':','=').replace("'",""))
        #     result = Commande.objects.filter(
        #     date=date,)
        print(final_data)
        context = {"result": final_data}
        return HttpResponse(json.dumps(context, indent=4, default=str), content_type="application/json")


def renouveler_contrat(request):
    return render(request, "commerciale/renouveler_contrat.html")


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
            data[i]['prix_unitaire'] = product.prix_unitaire
            i = i+1

        return HttpResponse(json.dumps(data, indent=4, default=str), content_type="application/json")

    else:
        raise Http404
