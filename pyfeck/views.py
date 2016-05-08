from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from pyfeck.models import CharacterClassCategory


def IndexView(request):
    return render(request, "pyfeck/index.html", context = {"output" : "Hello World!"})