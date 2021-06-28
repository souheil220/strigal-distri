from django.http import HttpResponse
from django.contrib.auth.models import Group


def distributeur(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            query_set = Group.objects.filter(user=request.user)
            profile = ""
            for g in query_set:
                profile = g
            print(type(profile.name))
            if profile.name == 'distributeur':
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Non autorisé')
    return wrapper_func
