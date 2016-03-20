from django.contrib import admin

# Register your models here.
from pyfeck.models import Weapon, WeaponRank, StatCategory, CharacterClassCategory, Skill


class Weapon_Inline(admin.TabularInline):
    model = Weapon
    extra = 1

class WeaponRank_Inline(admin.TabularInline):
    model = WeaponRank
    extra = 1

class StatCategory_Inline(admin.TabularInline):
    model = StatCategory
    extra = 1

class CharacterClassCategory_Inline(admin.TabularInline):
    model = CharacterClassCategory
    extra = 1

class Skill_Inline(admin.TabularInline):
    model = Skill
    extra = 1

admin.site.register(Skill)
admin.site.register(CharacterClassCategory)
admin.site.register(StatCategory)
admin.site.register(Weapon)
admin.site.register(WeaponRank)