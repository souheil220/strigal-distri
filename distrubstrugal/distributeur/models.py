from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Distributeur(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    typeProfile = models.CharField(max_length=255, default="Distributeur")
    nom = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    rcn = models.CharField(max_length=255)
    ifn = models.CharField(max_length=255)
    nbr_facture = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    reference_description = models.CharField(max_length=255)
    destributeur = models.ForeignKey(Distributeur, on_delete=models.CASCADE)
    societe = models.CharField(default='Strugal', max_length=255)
    totaleHT = models.FloatField()
    totaleTTC = models.FloatField()
    date = models.CharField(
        default=date.today().strftime("%d/%m/%Y"), max_length=255)


class Article(models.Model):
    id_article = models.CharField(max_length=255)
    nom_article = models.CharField(max_length=255)
    type_de_categorie = models.CharField(max_length=255)
    categorie_interne = models.CharField(max_length=255)
    famille_article = models.CharField(max_length=255)
    unite_mesure = models.CharField(max_length=255)
    sale_ok = models.BooleanField()
    type_article = models.CharField(max_length=255)
    template_id = models.IntegerField()
    company_id = models.IntegerField()
    active = models.BooleanField()
    product_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{}".format(self.id_article)


class ListArticleCommande(models.Model):
    id = models.AutoField(primary_key=True)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    code_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    qte = models.IntegerField()
    montant = models.FloatField()
