from django.db import models

class StatCategory(models.Model):
    name = models.CharField(max_length = 20)
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
    name = models.CharField(max_length = 20)
    rank = models.ForeignKey(WeaponRank, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class CharacterClassCategory(models.Model):
    name = models.CharField(max_length = 20)
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
    name = models.CharField(max_length = 10)
    class Meta:
        verbose_name = "Sex Category"
        verbose_name_plural = "Sex Categories"
    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length = 20)
    gender = models.ForeignKey(SexCategory, on_delete = models.CASCADE)
    baseLevel = models.IntegerField()
    skillName = models.CharField(max_length = 50)
    skillDescription = models.CharField(max_length = 500)
    currentClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    primaryClassCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE, related_name = "primary_Class_Category")
    secondaryClassCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE, related_name = "secondary_Class_Category")
    isCurrentClassPrimary = models.BooleanField()

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
    base_weapon_rank = models.ForeignKey(WeaponRank, on_delete = models.CASCADE)
    character = models.ForeignKey(Character, on_delete = models.CASCADE)

class CharacterStat(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    stat = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    growth = models.IntegerField()
    base = models.IntegerField()
    cap_modifier = models.IntegerField()

# TODO: Add character friendship classes, marriage classes
# TODO: Add child characters and make Gen 2 concept
# TODO: Add formula for child growths and stat cap modifiers and also bases
# TODO: Add Kamui talent
# TODO: Add boon and bane
# TODO: Add generational tags as well as 3rd gen malarkey