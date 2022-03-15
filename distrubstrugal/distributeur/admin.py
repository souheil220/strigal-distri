from django.contrib import admin
from .models import *


class FilterAricle(admin.ModelAdmin):
    list_display = ("product_id",
                    "nom_article",
                    "id_article",
                    "unite_mesure",
                    "conditionnement",
                    "prix_unitaire",
                    "id_154_surcharge",
                    "id_346_surcharge",
                    "id_347_surcharge",
                    "id_376_surcharge",
                    "id_154_prixparlist",
                    "id_346_prixparlist",
                    "id_347_prixparlist",
                    "id_376_prixparlist")


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
                    "n_commande_odoo",
                    "totaleHT",
                    "capture",
                    "etat",
                    "date")


class FilterListArticleCommande(admin.ModelAdmin):
    list_display = ("id",
                    "id_commande",
                    "code_article",
                    "qte",
                    "montant")


class FilterListeDesTarifs(admin.ModelAdmin):
    list_display = ("id",
                    "name")


class FilterCréerFacture(admin.ModelAdmin):
    list_display = ("id",
                    "policy")


class FilterVendeur(admin.ModelAdmin):
    list_display = ("id",
                    "name")


class FilterEquipeCommerciale(admin.ModelAdmin):
    list_display = ("id",
                    "code",
                    "name")


class FilterRegimeFiscal(admin.ModelAdmin):
    list_display = ("id",
                    "fiscal_position",
                    "name")


class FilterWarehouse(admin.ModelAdmin):
    list_display = ("id",
                    "code",
                    "name")


admin.site.register(Article, FilterAricle)
admin.site.register(Distributeur, FilterDistributeur)
admin.site.register(Commande, FilterCommande)
admin.site.register(ListArticleCommande, FilterListArticleCommande)
admin.site.register(ListeDesTarifs, FilterListeDesTarifs)
admin.site.register(CréerFacture, FilterCréerFacture)
admin.site.register(Vendeur, FilterVendeur)
admin.site.register(EquipeCommerciale, FilterEquipeCommerciale)
admin.site.register(RegimeFiscal, FilterRegimeFiscal)
admin.site.register(Warehouse, FilterWarehouse)
