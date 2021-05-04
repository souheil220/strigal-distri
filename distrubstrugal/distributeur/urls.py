from django.urls import path

from . import views

urlpatterns = [
    path("commande", views.commande, name="commande"),
    path("listCommandesD", views.listCommandes, name="listCommandesD"),
    path("detailCommande/<str:id>", views.detailCommande, name="detailCommande"),
    path("loadMore/<str:name>/<str:whiche>", views.loadMore, name="loadMore"),
    path("regCommand", views.regCommand, name="regCommand"),

]
