from django.db import models


class AbilityScore(models.Model):
    name = models.CharField(max_length=255)
    abbreviated_name = models.CharField(max_length=3)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255)
    ability_score = models.ForeignKey(AbilityScore, models.PROTECT)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class WeaponType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DamageType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(max_length=255)
    weapon_type = models.ForeignKey(WeaponType, models.PROTECT)
    cost = models.PositiveIntegerField()
    damage = models.CharField(max_length=10, null=True)
    damage_type = models.ForeignKey(DamageType, models.PROTECT)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)

    def __str__(self):
        return self.name


class WeaponProperty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class WeaponWeaponProperty(models.Model):
    weapon_id = models.ForeignKey(Weapon, models.CASCADE)
    property_id = models.ForeignKey(WeaponProperty, models.CASCADE)

    class Meta:
        unique_together = ('weapon_id', 'property_id')


class EquipmentCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    cost = models.PositiveIntegerField()
    equipment_category = models.ForeignKey(
        EquipmentCategory,
        on_delete=models.PROTECT
    )
    weight = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
