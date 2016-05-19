from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from pyfeck.models import  Character,Weapon, CharacterWeaponRank, StatCategory, CharacterStat, CharacterClassWeapon

from pyfeck.models import CharacterClassCategory


class IndexView(generic.ListView):
    template_name = 'pyfeck/index.html'
    context_object_name = 'all_characters'

    def get_queryset(self):
        return Character.objects.all()

class CharacterView(generic.DetailView):
    model = Character
    template_name = 'pyfeck/character.html'
    context_object_name="character"
    def get_values(self, character_id):
        return StatCategory.objects.get_all_for_character(character_id)
    def get_context_data(self, **kwargs):
        context=super(CharacterView,self).get_context_data(**kwargs)
        context["selectedClassId"]=int(self.kwargs["cpk"])
        # if self.model.objects.filter(character_id= self.kwargs["pk"],character_primaryClass__id=self.kwargs["cpk"]).count()==1:
        #     context["primaryClassSelected"] ="checked"
        #     context["secondaryClassSelected"]=""
        # elif self.model.secondaryClass_id==self.kwargs["cpk"]:
        #     context["primaryClassSelected"] =""
        #     context["secondaryClassSelected"]="checked"
        # else:
        #     context["primaryClassSelected"] =""
        #     context["secondaryClassSelected"]=""
        context["classWeapons"]=CharacterClassWeapon.objects.filter(characterClass_id=self.kwargs["cpk"])
        context["statCategories"]=self.get_values(self.kwargs["pk"])
        context["statCategory"]=StatCategory.objects.first()
        context["characterStats"]=CharacterStat.objects.filter(character_id=self.kwargs["pk"])
        context["characterStat"]=CharacterStat.objects.first()
        return context

class WeaponView(generic.DetailView):
    model = Weapon
    template_name = 'pyfeck/weapon.html'

def ClassView(request,pk):
    return HttpResponse("Character details for class: " + pk)
