from django.db import models
from datetime import date


class Distributeur(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    rcn = models.CharField(max_length=255)
    ifn = models.CharField(max_length=255)
    nbr_facture = models.IntegerField()


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    reference_description = models.CharField(max_length=255)
    destributeur = models.ForeignKey(Distributeur, on_delete=models.CASCADE)
    societe = models.CharField(default='Strugal', max_length=255)
    totaleHT = models.FloatField()
    totaleTTC = models.FloatField()
    date = models.CharField(
        default=date.today().strftime("%d/%m/%Y"), max_length=255)


class ListArticleCommande(models.Model):
    id = models.AutoField(primary_key=True)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    code_article = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    qte = models.IntegerField()
    montant = models.FloatField()
