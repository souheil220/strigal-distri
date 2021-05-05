from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.test, name="login"),
    path("logout", views.logoutUser, name="logout"),
]
