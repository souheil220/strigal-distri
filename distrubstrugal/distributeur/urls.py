from django.urls import path

from . import views

urlpatterns = [
    path("commande", views.commande, name="commande"),
    path("listCommandesD", views.listCommandes, name="listCommandesD"),
    path("loadMore/<str:name>", views.loadMore, name="loadMore"),
    path("regCommand", views.regCommand, name="regCommand"),

]
