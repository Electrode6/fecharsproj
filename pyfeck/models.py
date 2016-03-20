from django.db import models

class StatCategory(models.Model):
    name = models.CharField(max_length = 20)
    class Meta:
        verbose_name = "Stat Category"
        verbose_name_plural = "Stat Categories"
    def __str__(self):
        return self.name

class Stat(models.Model):
    statCategory = models.ForeignKey(StatCategory, on_delete = models.CASCADE)
    growth = models.IntegerField()

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

class CharacterClassCategoryPromotion(models.Model):
    fromCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE, related_name = "from_category")
    toCategory = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE, related_name = "to_category")

class Skill(models.Model):
    name = models.CharField(max_length = 50)
    category = models.ForeignKey(CharacterClassCategory, on_delete = models.CASCADE)
    minLevel = models.IntegerField()
    description = models.CharField(max_length = 500)
    def __str__(self):
        return self.name

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
    # secondaryClassCategory = models.ForeignKey()