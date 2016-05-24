from django.db import models

class StatCategoryCharacter:
    def __init__(self, stat_name, base, character_growth, character_cap_modifier,class_growth,class_cap,guardStanceBonus):
        self.statName=stat_name
        self.base=base
        self.character_growth=character_growth
        self.character_capModifier=character_cap_modifier
        self.class_growth=class_growth
        self.class_cap=class_cap
        self.guardStanceBonus=guardStanceBonus

class StatCategoryManager(models.Manager):
    def get_all_for_character_and_class(self, character_id, class_id):
        characterStats = CharacterStat.objects.filter(character_id=character_id)
        classStats=CharacterClassStat.objects.filter(characterClass_id=class_id)
        statCategoriesCharacter=[]
        for statCategory in self.all():
            character_growth_for_stat=0
            character_base_for_stat=0
            character_capModifier_for_stat=0
            class_growth = 0
            class_cap = 0
            class_guardStanceBonus = 0

            if characterStats.filter(stat_id=statCategory.pk).count()>0:
                characterStat=characterStats.filter(stat_id=statCategory.pk).first()
                character_growth_for_stat=characterStat.growth
                character_base_for_stat=characterStat.base
                character_capModifier_for_stat=characterStat.cap_modifier
            if classStats.filter(stat_id=statCategory.pk).count()>0:
                classStat=classStats.filter(stat_id=statCategory.pk).first()
                class_growth=classStat.growth
                class_cap=classStat.cap
                class_guardStanceBonus=classStat.guardStanceBonus
            statCategoriesCharacter.append(StatCategoryCharacter(statCategory.name,character_base_for_stat,character_growth_for_stat,character_capModifier_for_stat,class_growth,class_cap,class_guardStanceBonus))
        return statCategoriesCharacter

#presented through UI
class StatCategory(models.Model):
    name = models.CharField(max_length = 20, verbose_name="stat")
    objects=StatCategoryManager()
    class Meta:
        verbose_name = "Stat Category"
        verbose_name_plural = "Stat Categories"
    def __str__(self):
        return self.name

#presented through UI
class WeaponRank(models.Model):
    name = models.CharField(max_length = 1)
    order = models.IntegerField()
    def __str__(self):
        return self.name

#presented through UI
class Weapon(models.Model):
    name = models.CharField(max_length = 20, verbose_name="name")
    image_static=models.CharField(max_length=256)
    def __str__(self):
        return self.name

#presented through UI
class CharacterClassCategory(models.Model):
    name = models.CharField(verbose_name="class name", max_length = 20)
    class Meta:
        verbose_name = "Character Class Category"
        verbose_name_plural = "Character Class Categories"
    def __str__(self):
        return self.name

class CharacterClassCategoryRelation(models.Model):
    fromClassCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE, related_name = "from_Class_Category")
    toClassCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE, related_name = "to_Class_Category")

class CompoundStatCategory(models.Model):
    name = models.CharField(max_length = 20)
    class Meta:
        verbose_name = "Compound Stat Category"
        verbose_name_plural = "Compound Stat Categories"
    def __str__(self):
        return self.name

class CharacterClass(models.Model):
    category = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE)
    tier = models.IntegerField()
    class Meta:
        verbose_name_plural = "Character Classes"
    def __str__(self):
        return self.category.name

class CharacterClassCompoundStat(models.Model):
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    compoundStatCategory = models.ForeignKey(CompoundStatCategory, on_delete = models.CASCADE)
    bonus = models.IntegerField()

#presented through UI
class CharacterClassStat(models.Model):
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    stat = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    growth = models.IntegerField(verbose_name="growth")
    cap = models.IntegerField(verbose_name="cap")
    guardStanceBonus = models.IntegerField(verbose_name="guard stance bonus")
    def __str__(self):
        return self.characterClass.category.name + " - " + self.stat.name

class CharacterClassPromotion(models.Model):
    fromClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE, related_name = "from_class")
    toClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE, related_name = "to_class")

#presented through UI
class CharacterClassWeapon(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete = models.CASCADE)
    max_weapon_rank = models.ForeignKey(WeaponRank, on_delete = models.CASCADE)
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)

    def __str__(self):
        return self.characterClass.category.name + " - " + self.weapon.name

class CharacterClassBonuses(models.Model):
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    # stat = models.ForeignKey(Stat, on_delete = models.CASCADE)

#Presented through UI
class CharacterClassSkill(models.Model):
    name = models.CharField(max_length = 50)
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    minLevel = models.IntegerField()
    description = models.CharField(max_length = 500)
    def __str__(self):
        return self.name

class SupportLevelAvailability(models.Model):
    description = models.CharField(max_length = 20)
    class Meta:
        verbose_name = "Support Level Availability"
        verbose_name_plural = "Support Level Availabilities"
    def __str__(self):
        return self.description

class SupportLevel(models.Model):
    name = models.CharField(max_length = 2)
    availability = models.ForeignKey(SupportLevelAvailability, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

#presented through UI
class SexCategory(models.Model):
    name = models.CharField(verbose_name="sex",max_length = 10)
    class Meta:
        verbose_name = "Sex Category"
        verbose_name_plural = "Sex Categories"
    def __str__(self):
        return self.name

#presented through UI
class Character(models.Model):
    name = models.CharField(max_length = 20)
    gender = models.ForeignKey(SexCategory, on_delete = models.CASCADE)
    baseLevel = models.IntegerField(verbose_name='base level')
    maxLevel=models.IntegerField(verbose_name='max level')
    skillName = models.CharField(verbose_name="character skill", max_length = 50)
    skillDescription = models.CharField(max_length = 500)
    primaryClass = models.ForeignKey(CharacterClass, verbose_name="primary class", on_delete = models.CASCADE, related_name = "primary_Class")
    secondaryClass = models.ForeignKey(CharacterClass, verbose_name="secondary class",on_delete = models.CASCADE, related_name = "secondary_Class")
    generationChoices = ((1, "Generation One"), (2, "Generation Two"), (3, "Generation Three"))
    generation = models.IntegerField(verbose_name="generation", choices = generationChoices, default = 1)
    image_static = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class CharacterSupportLevelStatBonus(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    supportLevel = models.ForeignKey(SupportLevel, on_delete = models.CASCADE)
    stat = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    attackStanceBonus = models.IntegerField()
    guardStanceBonus = models.IntegerField()

class CharacterRelationship(models.Model):
    supportingCharacter = models.ForeignKey(Character, on_delete = models.CASCADE, related_name = "supporting_Character")
    supportedCharacter = models.ForeignKey(Character, on_delete = models.CASCADE, related_name = "supported_Character")
    supportLevel = models.ForeignKey(SupportLevel, on_delete = models.CASCADE)
    dependentCharacter = models.ForeignKey(Character, on_delete = models.CASCADE, related_name = "dependent_Character")

#presented through UI
class CharacterPrimaryClassWeapon(models.Model):
    classWeapon=models.ForeignKey(CharacterClassWeapon)
    base_weapon_rank = models.ForeignKey(WeaponRank, on_delete = models.CASCADE,verbose_name="character base rank for weapon")
    character=models.ForeignKey(Character)

#presented through UI
class CharacterStat(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    stat = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    growth = models.IntegerField(verbose_name="personal growth")
    base = models.IntegerField( verbose_name="base")
    cap_modifier = models.IntegerField(verbose_name="cap modifier")


# TODO: Add character friendship classes, marriage classes
# TODO: Add formula for child growths and stat cap modifiers and also bases and class sets from parents
# TODO: Add Kamui talent
# TODO: Add boon and bane