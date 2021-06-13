from django.contrib import admin
from .models import *


class FilterAricle(admin.ModelAdmin):
    list_display = ("id_article",
                    "nom_article",
                    "type_de_categorie",
                    "categorie_interne",
                    "famille_article",
                    "unite_mesure",
                    "sale_ok",
                    "type_article",
                    "template_id",
                    "company_id",
                    "active",
                    "product_id",
                    "prix_unitaire")


class FilterDistributeur(admin.ModelAdmin):
    list_display = ("id",
                    "user",
                    "nom",
                    "adress",
                    "tel_fix",
                    "tel_portable",
                    "couriel",
                    "date_effet",
                    "date_echeance",
                    "status",
                    "nbr_facture")


class FilterCommande(admin.ModelAdmin):
    list_display = ("id",
                    "reference_description",
                    "destributeur",
                    "societe",
                    "totaleHT",
                    "totaleTTC",
                    "capture",
                    "date")


class FilterListArticleCommande(admin.ModelAdmin):
    list_display = ("id",
                    "id_commande",
                    "code_article",
                    "qte",
                    "montant")


admin.site.register(Article, FilterAricle)
admin.site.register(Distributeur, FilterDistributeur)
admin.site.register(Commande, FilterCommande)
admin.site.register(ListArticleCommande, FilterListArticleCommande)
