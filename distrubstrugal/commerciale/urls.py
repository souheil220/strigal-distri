from django.urls import path

from . import views

urlpatterns = [
    path("listCommandesC", views.listCommandes, name="listCommandes"),
    path("detailCommande/<str:id>", views.detailCommande, name="detailCommande"),
    path("loadMore/<str:name>", views.loadMore, name="loadMore"),
    path("renew", views.renew, name="renew"),
    path("renouvelerContrat", views.renouveler_contrat, name="renouveler_contrat"), ]
