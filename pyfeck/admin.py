from django.contrib import admin

# Register your models here.
from pyfeck.models import Weapon, WeaponRank, StatCategory, CharacterClassCategory, CharacterClassStat, \
    CharacterClass, CompoundStatCategory, CharacterClassCompoundStat, CharacterClassWeapon, CharacterClassPromotion, CharacterClassSkill, Character, \
    SexCategory, CharacterStat, SupportLevelAvailability, SupportLevel, \
    CharacterSupportLevelStatBonus, CharacterRelationship, CharacterPrimaryClassWeapon


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

class CharacterStat_Inline(admin.TabularInline):
    model = CharacterStat
    extra = 9

class CharacterSupportLevelStatBonus_Inline(admin.TabularInline):
    model = CharacterSupportLevelStatBonus
    extra = 1

class CharacterRelationship_Inline(admin.TabularInline):
    model = CharacterRelationship
    extra = 1
    fk_name = "supportingCharacter"

class CharacterClassAdmin(admin.ModelAdmin):
    fieldsets = [("Generic", {"fields" : ["category", "tier"]})]
    inlines = [CharacterClassStat_Inline, CharacterClassCompoundStat_Inline, CharacterClassWeapon_Inline, CharacterClassPromotion_Inline, CharacterClassSkill_Inline]


class CharacterPrimaryClassWeaponAdmin(admin.TabularInline):
    list_display=("character","classWeapon","base_weapon_rank")
    fields=("character","classWeapon", "base_weapon_rank")
    model = CharacterPrimaryClassWeapon
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "classWeapon":
            kwargs["queryset"] = CharacterClassWeapon.objects.order_by("characterClass")
        return super(CharacterPrimaryClassWeaponAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [("Generic", {"fields" : ["name", "gender", "baseLevel", "skillName", "skillDescription", "primaryClass", "secondaryClass","generation"]})]
    inlines = [CharacterPrimaryClassWeaponAdmin, CharacterStat_Inline, CharacterSupportLevelStatBonus_Inline, CharacterRelationship_Inline]

class SupportLevelAvailability_Inline(admin.TabularInline):
    model = SupportLevelAvailability
    extra = 1

class SupportLevel_Inline(admin.TabularInline):
    model = SupportLevel
    extra = 1

class GenderAdmin(admin.TabularInline):
    model = SexCategory
    extra = 1

# admin.site.register(CharacterPrimaryClassWeapon, CharacterPrimaryClassWeaponAdmin)
admin.site.register(SupportLevel)
admin.site.register(SupportLevelAvailability)
admin.site.register(SexCategory)
admin.site.register(Character, CharacterAdmin)
admin.site.register(CompoundStatCategory)
admin.site.register(CharacterClass, CharacterClassAdmin)
admin.site.register(CharacterClassCategory)
admin.site.register(StatCategory)
admin.site.register(Weapon)
admin.site.register(WeaponRank)

