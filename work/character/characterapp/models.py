from django.db import models

# Create your models here.

class Weapon(models.Model):
    name = models.CharField(max_length=30)
    attack = models.PositiveBigIntegerField()
    defense = models.PositiveBigIntegerField()
    attack_per_round = models.FloatField()

    def __str__(self) -> str:
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=30)
    strength = models.PositiveBigIntegerField()
    dexterity = models.PositiveBigIntegerField()
    constitution = models.PositiveBigIntegerField()
    intelligence = models.PositiveBigIntegerField()
    wisdom = models.PositiveBigIntegerField()
    charisma = models.PositiveBigIntegerField()
    weapons = models.ManyToManyField(Weapon, blank=True)

    def __str__(self) -> str:
        return self.name