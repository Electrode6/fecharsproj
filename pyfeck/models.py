from django.db import models

class StatCategoryCharacter:
    def __init__(self, stat_name,base,growth,cap_modifier):
        self.statName=stat_name
        self.base=base
        self.growth=growth
        self.capModifier=cap_modifier

class StatCategoryManager(models.Manager):
    def get_all_for_character(self, character_id):
        characterStats = CharacterStat.objects.filter(character_id=character_id)
        statCategoriesCharacter=[]
        for statCategory in self.all():
            growth_for_stat=0
            base_for_stat=0
            capModifier_for_stat=0
            if characterStats.filter(stat_id=statCategory.pk).count()>0:
                characterStat=characterStats.filter(stat_id=statCategory.pk).first()
                growth_for_stat=characterStat.growth
                base_for_stat=characterStat.base
                capModifier_for_stat=characterStat.cap_modifier

            statCategoriesCharacter.append(StatCategoryCharacter(statCategory.name,base_for_stat,growth_for_stat,capModifier_for_stat))
        return statCategoriesCharacter

class StatCategory(models.Model):
    name = models.CharField(max_length = 20, verbose_name="stat")
    objects=StatCategoryManager()
    class Meta:
        verbose_name = "Stat Category"
        verbose_name_plural = "Stat Categories"
    def __str__(self):
        return self.name

class WeaponRank(models.Model):
    name = models.CharField(max_length = 1)
    order = models.IntegerField()
    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length = 20, verbose_name="name")
    image_static=models.CharField(max_length=256)
    def __str__(self):
        return self.name

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

class CharacterClassStat(models.Model):
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    stat = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    growth = models.IntegerField()
    cap = models.IntegerField()
    guardStanceBonus = models.IntegerField()
    def __str__(self):
        return self.characterClass.category.name + " - " + self.stat.name

class CharacterClassPromotion(models.Model):
    fromClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE, related_name = "from_class")
    toClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE, related_name = "to_class")

class CharacterClassWeapon(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete = models.CASCADE)
    max_weapon_rank = models.ForeignKey(WeaponRank, on_delete = models.CASCADE)
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)

class CharacterClassBonuses(models.Model):
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    # stat = models.ForeignKey(Stat, on_delete = models.CASCADE)

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

class SexCategory(models.Model):
    name = models.CharField(verbose_name="sex",max_length = 10)
    class Meta:
        verbose_name = "Sex Category"
        verbose_name_plural = "Sex Categories"
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length = 20)
    gender = models.ForeignKey(SexCategory, on_delete = models.CASCADE)
    baseLevel = models.IntegerField(verbose_name='base level')
    skillName = models.CharField(verbose_name="skill", max_length = 50)
    skillDescription = models.CharField(max_length = 500)
    primaryClass = models.ForeignKey(CharacterClass, verbose_name="primary class", on_delete = models.CASCADE, related_name = "primary_Class")
    secondaryClass = models.ForeignKey(CharacterClass, verbose_name="secondary class",on_delete = models.CASCADE, related_name = "secondary_Class")
    generationChoices = ((1, "Generation One"), (2, "Generation Two"), (3, "Generation Three"))
    generation = models.IntegerField(verbose_name="generation", choices = generationChoices, default = 1)
    image_static = models.CharField(max_length=255)

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

class CharacterWeaponRank(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete = models.CASCADE)
    base_weapon_rank = models.ForeignKey(WeaponRank, on_delete = models.CASCADE,verbose_name="character base rank for weapon")
    character = models.ForeignKey(Character, on_delete = models.CASCADE)

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