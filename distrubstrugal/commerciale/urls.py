from django.urls import path

from . import views

urlpatterns = [
    path("listCommandesC", views.listCommandes, name="listCommandes"),
    path("suiviContrat", views.suiviContrat, name="suiviContrat"),
    path("detailCommande/<str:id>", views.detailCommande, name="detailCommande"),
    path("detailDisti/<str:id>", views.detailDisti, name="detailDisti"),
    path("loadMore/<str:argum>/<str:whicheone>",
         views.loadMore, name="loadMore"),
    path("filterer/<str:dist>/<str:date>",
         views.filterer, name="filterer"),
    path("filtererListCommand/<str:dist>/<str:date>/<str:etat>/<str:refdes>",
         views.filtererListCommand, name="filtererListCommand"),
    path("renew", views.renew, name="renew"),
    path("renouvelerContrat", views.renouveler_contrat, name="renouveler_contrat"),
    path("annulerCommande/<str:id>", views.annulerCommande, name="annulerCommande"),
    path("ajouterDis", views.ajouterDis, name="ajouterDis"), ]
