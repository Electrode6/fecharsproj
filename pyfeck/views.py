from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from pyfeck.models import  Character,Weapon, StatCategory, CharacterStat, CharacterClassWeapon, \
    CharacterPrimaryClassWeapon, CharacterClassStat, CharacterClassSkill

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
    def get_values(self, character_id, class_id):
        return StatCategory.objects.get_all_for_character_and_class(character_id, class_id)
    def get_context_data(self, **kwargs):
        context=super(CharacterView,self).get_context_data(**kwargs)
        context["selectedClassId"]=int(self.kwargs["cpk"])
        context["selectedLevel"]=int(self.kwargs["lpk"])
        context["characterWeapons"]=CharacterPrimaryClassWeapon.objects.filter(character_id=self.kwargs["pk"])
        context["statCategories"]=self.get_values(self.kwargs["pk"],self.kwargs["cpk"])
        context["statCategory"]=StatCategory.objects.first()
        context["characterStat"]=CharacterStat.objects.first()
        context["classStat"]=CharacterClassStat.objects.first()
        context["classSkills"]=CharacterClassSkill.objects.filter(characterClass_id=self.kwargs["cpk"], minLevel__lte=int(self.kwargs["lpk"]))
        return context

class WeaponView(generic.DetailView):
    model = Weapon
    template_name = 'pyfeck/weapon.html'

def ClassView(request,pk):
    return HttpResponse("Character details for class: " + pk)
