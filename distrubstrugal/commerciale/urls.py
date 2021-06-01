from django.urls import path

from . import views

urlpatterns = [
    path("listCommandesC", views.listCommandes, name="listCommandes"),
    path("suiviContrat", views.suiviContrat, name="suiviContrat"),
    path("detailCommande/<str:id>", views.detailCommande, name="detailCommande"),
    path("loadMore/<str:name>", views.loadMore, name="loadMore"),
    path("filterer/<str:dist>/<str:date>", views.filterer, name="filterer"),
    path("renew", views.renew, name="renew"),
    path("renouvelerContrat", views.renouveler_contrat, name="renouveler_contrat"),
    path("annulerCommande/<str:id>", views.annulerCommande, name="annulerCommande"),
    path("ajouterDis", views.ajouterDis, name="ajouterDis"), ]
