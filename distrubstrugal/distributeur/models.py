import code
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Distributeur(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    id_dist = models.IntegerField(default=0)
    nom = models.CharField(max_length=255)
    adress = models.CharField(max_length=255)
    tel_fix = models.CharField(null=True, blank=True, max_length=255)
    tel_portable = models.CharField(null=True, blank=True, max_length=255)
    couriel = models.CharField(null=True, blank=True, max_length=255)
    civilite = models.IntegerField(null=True, blank=True)
    site_web = models.CharField(null=True, blank=True, max_length=255)
    rcn = models.CharField(max_length=255)
    date_enregistrement_rc = models.CharField(max_length=255)
    nis = models.CharField(null=True, blank=True, max_length=255)
    ifn = models.CharField(max_length=255)
    art = models.CharField(max_length=255)
    date_debut_activité = models.CharField(
        null=True, blank=True, max_length=255)
    date_effet = models.CharField(null=True, blank=True, max_length=255)
    date_echeance = models.CharField(null=True, blank=True, max_length=255)
    status = models.CharField(max_length=255)
    nbr_facture = models.IntegerField(default=0)

    def __str__(self):
        return self.nom


class ListeDesTarifs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)


class CréerFacture(models.Model):
    id = models.AutoField(primary_key=True)
    policy = models.CharField(max_length=255, null=True, blank=True)


class Vendeur(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)


class EquipeCommerciale(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)


class RegimeFiscal(models.Model):
    id = models.AutoField(primary_key=True)
    fiscal_position = models.IntegerField()
    name = models.CharField(max_length=255, null=True, blank=True)


class Warehouse(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)


class Commande(models.Model):
    id = models.AutoField(primary_key=True)
    n_commande_odoo = models.CharField(null=True, blank=True, max_length=255)
    reference_description = models.CharField(max_length=255)
    destributeur = models.ForeignKey(Distributeur, on_delete=models.CASCADE)
    societe = models.CharField(default='Strugal', max_length=255)
    totaleHT = models.FloatField()
    capture = models.ImageField(
        upload_to='emailCapture/', null=True, blank=True)
    list_des_prix = models.ForeignKey(
        ListeDesTarifs, on_delete=models.CASCADE, null=True, blank=True)
    regime_fiscal = models.ForeignKey(
        RegimeFiscal, on_delete=models.CASCADE, null=True, blank=True)
    creer_facture = models.ForeignKey(
        CréerFacture, on_delete=models.CASCADE, null=True, blank=True)
    equipe_commerciale = models.ForeignKey(
        EquipeCommerciale, on_delete=models.CASCADE, null=True, blank=True)
    vendeur = models.ForeignKey(
        Vendeur, on_delete=models.CASCADE, null=True, blank=True)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, null=True, blank=True)
    etat = models.CharField(default='Brouillon', max_length=255)
    date = models.CharField(max_length=255)


class Article(models.Model):
    product_id = models.IntegerField(primary_key=True)
    nom_article = models.CharField(max_length=255)
    id_article = models.CharField(max_length=255)
    unite_mesure = models.CharField(max_length=255)
    conditionnement = models.CharField(max_length=255, null=True, blank=True)
    prix_unitaire = models.FloatField(default=0)
    id_154_surcharge = models.FloatField(default=0)
    id_346_surcharge = models.FloatField(default=0)
    id_347_surcharge = models.FloatField(default=0)
    id_376_surcharge = models.FloatField(default=0)
    id_154_prixparlist = models.FloatField(default=0)
    id_346_prixparlist = models.FloatField(default=0)
    id_347_prixparlist = models.FloatField(default=0)
    id_376_prixparlist = models.FloatField(default=0)
    

    def __str__(self):
        return "{}".format(self.id_article)


class ListArticleCommande(models.Model):
    id = models.AutoField(primary_key=True)
    id_commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    code_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    qte = models.IntegerField()
    prix_unitaire = models.IntegerField(default=0)
    montant = models.FloatField()
