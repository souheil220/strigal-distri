from django.shortcuts import render

# Create your views here.


def listCommandes(request):
    return render(
        request, "commerciale/listCommandes.html", {

        })
