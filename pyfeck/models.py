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

class SexCategory(models.Model):
    name = models.CharField(max_length = 10)

class Character(models.Model):
    name = models.CharField(max_length = 20)
    gender = models.ForeignKey(SexCategory, on_delete = models.CASCADE)
    baseLevel = models.IntegerField()
    skillName = models.CharField(max_length = 50)
    skillDescription = models.CharField(max_length = 500)
    primaryClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    # secondaryClass = models.ForeignKey()

class CharacterStatGrowth(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    stat = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    growth = models.IntegerField()

class CharacterStatBase(models.Model):
    character = models.ForeignKey(Character, on_delete = models.CASCADE)
    stat = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    value = models.IntegerField()

# TODO: Add base character weapon ranks
# TODO: Add stat cap modifiers
# TODO: Add class stat caps
# TODO: Add character stat growths and base stats
# TODO: Add each characters' supportables
# TODO: Add AS and GS bonuses and tie to support levels
# TODO: Add character secondary classes, friendship classes, marriage classes
# TODO: Add child characters and make Gen 2 concept
#