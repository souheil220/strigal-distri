from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from distributeur.models import Commande, ListArticleCommande, Distributeur, Article
import json
import requests
from django.db.models import Q
from django.http import Http404, HttpResponse
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import openpyxl
from django.contrib.auth.decorators import login_required
from .decorators import commercial
# Create your views here.


def list_destri():
    try:
        pload = {'data': {}}
        print(pload)
        eleme = requests.post(
            "http://10.10.10.64:8180/diststru/", json=pload).json()
        print(eleme)
        s = "_"
        mail = ""
        for key in eleme.keys():
            print(eleme[key][7])
            if eleme[key][7] is not None and '@' in eleme[key][7]:
                print("i'm here")
                x = eleme[key][7].split('@')
                mail = eleme[key][7]
                s = x[0]
                print(x)
                print(mail)
                print(s)
            else:
                x = eleme[key][3].split()
                if '-' in x[0]:
                    x[0] = x[0].replace('-', '_')
                s = "_"
                s = s.join(x)
                print(s)

            utilisateur = User.objects.create_user(s, mail, 'Azerty@22')

            user = utilisateur
            id_dist = eleme[key][2]
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
                                        id_dist=id_dist,
                                        status=status
                                        )
            distributeur.save()

    except Exception as e:
        print('error', e)


@ login_required(login_url='login')
@commercial
def listCommandes(request):
    # list_destri()

    commande = Commande.objects.all().order_by('id')
    paginator = Paginator(commande, 5)
    page = request.GET.get('page')
    commande = paginator.get_page(page)
    context = {
        "commande": commande
    }

    return render(
        request, "commerciale/listCommandes.html", context)


@ login_required(login_url='login')
@commercial
def renouveler_contrat(request):
    return render(request, "commerciale/renouveler_contrat.html")


@ login_required(login_url='login')
@commercial
def ajouterDis(request):

    if request.method == 'POST':
        nom = request.POST['nom']
        nom_utilisateur = request.POST['nom_utilisateur']
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
        try:
            user = User.objects.get(username=nom_utilisateur)
            messages.error(
                request, 'Utilisateur existe deja')
        except:
            print("user does not exist")
            utilisateur = User.objects.create_user(
                nom_utilisateur, couriel, 'Azerty@22')
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


@ login_required(login_url='login')
@commercial
def suiviContrat(request):
    distributeur = Distributeur.objects.all()[:5].values(
        'id', 'nom', 'date_effet', 'date_echeance')
    print(distributeur)
    context = {
        'distributeur': distributeur
    }
    return render(request, 'commerciale/suivi_contrat.html', context)


@ login_required(login_url='login')
@commercial
def uploadProduct(request):
    if request.method == 'POST':
        try:
            excel_file = request.FILES['product']
            if (str(excel_file).split('.')[-1] == 'xls' or str(excel_file).split('.')[-1] == "xlsx"):
                wb = openpyxl.load_workbook(excel_file, data_only=True)
                worksheet = wb.active

            excel_data = list()
            # iterating over the rows and
            # getting value from each cell in row
            for row in list(worksheet.rows)[1:]:
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))

                excel_data.append(row_data)

            for produit in excel_data:
                id_article = produit[0]
                nom_article = produit[2]
                unite_mesure = produit[3]
                product_id = produit[1]
                prix_unitaire = produit[4]
                if (id_article != 'None' and nom_article != 'None' and unite_mesure != 'None' and product_id != 'None' and prix_unitaire != 'None'):
                    article = Article(id_article=id_article,
                                      nom_article=nom_article,
                                      unite_mesure=unite_mesure,
                                      product_id=product_id,
                                      prix_unitaire=prix_unitaire)

                    article.save()

        except:
            messages.error(
                request, 'Veillez uploader un fichier valide')
            return render(request, 'commerciale/uploadProduct.html')

    return render(request, 'commerciale/uploadProduct.html')


@ login_required(login_url='login')
@commercial
def donnerPermission(request):
    if request.method == 'POST':
        ad2000 = request.POST['ad2000']
        email = request.POST['email']
        utilisateur = User.objects.create_user(ad2000, email, 'Azerty@22')
        utilisateur.save()
        group = Group.objects.get(name='commercial')
        utilisateur.groups.add(group)
        return redirect('listCommandes')
    return render(
        request, "commerciale/donner_permission.html")


def annulerCommande(request, id):
    commande = Commande.objects.get(id=id)
    commande.etat = 'Annuler'
    commande.save()
    return redirect('listCommandes')


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
        'id_commande__capture',
        "code_article__unite_mesure",
        "id_commande__totaleHT",
        "id_commande__n_commande_odoo",
        "montant")
    print(list_commande[0]['id_commande__capture'])
    tva = int(list_commande[0]["id_commande__totaleHT"]) * 19 / 100
    context = {"id": id,
               'list_commande': list_commande,
               'totalTTC': list_commande[0]['id_commande__totaleTTC'],
               'capture': list_commande[0]['id_commande__capture'],
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
            result = Distributeur.objects.filter(nom__icontains=argum)[:5]

            print(result)
            data = {}
            i = 0
            for user in result:
                data[i] = {}
                data[i]['id_ditributeur'] = user.id_dist
                data[i]['nom_ditributeur'] = user.nom
                i = i+1

        else:
            result = Commande.objects.filter(
                reference_description__icontains=argum)[:5]

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


def loadMore(request, name, whiche):
    if request.is_ajax and request.method == "GET":
        if(whiche == "1"):
            result = Article.objects.filter(nom_article__icontains=name)[:5]
        else:
            result = Article.objects.filter(id_article__icontains=name)[:5]

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
