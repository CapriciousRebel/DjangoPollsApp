from django.shortcuts import render

# Views = Controller


from django.http import HttpResponse


def index(request):
    return HttpResponse("Shop")
