from django.contrib import admin

# Register your models here.
from pyfeck.models import Weapon, WeaponRank, StatCategory, CharacterClassCategory, CharacterClassStat, \
    CharacterClass, CompoundStatCategory, CharacterClassCompoundStat, CharacterClassWeapon, CharacterClassPromotion, CharacterClassSkill

class CharacterClassPromotion_Inline(admin.TabularInline):
    model = CharacterClassPromotion
    extra = 1
    fk_name = "toClass"

class CharacterClassCompoundStat_Inline(admin.TabularInline):
    model = CharacterClassCompoundStat
    extra = 1

class CompoundStatCategory_Inline(admin.TabularInline):
    model = CompoundStatCategory
    extra = 1

class CharacterClassWeapon_Inline(admin.TabularInline):
    model = CharacterClassWeapon
    extra = 1

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

class CharacterClassStat_Inline(admin.TabularInline):
    model = CharacterClassStat
    extra = 9

class CharacterClassSkill_Inline(admin.TabularInline):
    model = CharacterClassSkill
    extra = 2

class CharacterClassAdmin(admin.ModelAdmin):
    fieldsets = [("Generic", {"fields" : ["category", "tier"]})]
    inlines = [CharacterClassStat_Inline, CharacterClassCompoundStat_Inline, CharacterClassWeapon_Inline, CharacterClassPromotion_Inline, CharacterClassSkill_Inline]

admin.site.register(CompoundStatCategory)
admin.site.register(CharacterClass, CharacterClassAdmin)
admin.site.register(CharacterClassCategory)
admin.site.register(StatCategory)
admin.site.register(Weapon)
admin.site.register(WeaponRank)