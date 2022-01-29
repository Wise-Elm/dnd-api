from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=255)
    ability_score = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class WeaponProperty(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
