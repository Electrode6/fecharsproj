from django.db import models

class StatCategory(models.Model):
    name = models.CharField(max_length = 20)

class Stat(models.Model):
    statCategory = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    value = models.IntegerField()

class Weapon(models.Model):
    name = models.CharField(max_length = 20)

class CharacterClassCategory(models.Model):
    name = models.CharField(max_length = 20)

class CharacterClassCategoryPromotion(models.Model):
    fromCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE)
    toCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE)

class Skill(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE)
    minLevel = models.IntegerField()
    description = models.CharField(max_length = 500)

class CharacterClass(models.Model):
    category = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE)
    passive = models.IntegerField()
    tier = models.IntegerField()

class CharacterClassStat(models.Model):
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    stat = models.ForeignKey(Stat, on_delete = models.CASCADE)

class CharacterClassWeapon(models.Model):
    weapon = models.ForeignKey(Weapon, on_delete = models.CASCADE)
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)

class CharacterClassBonuses(models.Model):
    characterClass = models.ForeignKey(CharacterClass, on_delete = models.CASCADE)
    stat = models.ForeignKey(Stat, on_delete = models.CASCADE)

class Character(models.Model):
    name = models.CharField(max_length = 20)
    level = models.IntegerField()
    primaryClassCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE)
    secondaryClassCategory = models.ForeignKey()