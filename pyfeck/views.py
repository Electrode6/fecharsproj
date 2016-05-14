from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from pyfeck.models import Character
from pyfeck.models import CharacterClassCategory


class IndexView(generic.ListView):
    template_name = "pyfeck/index.html"
    context_object_name = "allCharacters"
    def get_queryset(self):
        return Character.objects.all()

class CharacterView(generic.DetailView):
    template_name = "pyfeck/character.html"
    model = Character