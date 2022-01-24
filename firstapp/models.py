from django.db import models


class EquipmentCategory(models.Model):
    title = models.CharField(max_length=255)


class GearCategory(models.Model):
    title = models.CharField(max_length=255)


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    weight = models.PositiveSmallIntegerField()
    equipment_category = \
        models.OneToOneField(EquipmentCategory, on_delete=models.CASCADE, primary_key=True)
    gear_category = \
        models.OneToOneField(GearCategory, on_delete=models.CASCADE)


class Price(models.Model):
    quantity = models.PositiveSmallIntegerField()
    cost_unit_type = models.CharField(max_length=5)
    equipment = \
        models.OneToOneField(Equipment, on_delete=models.CASCADE, primary_key=True)


class UserCollection(models.Model):
    title = models.CharField(max_length=255)


class CollectionItem(models.Model):
    user_collection = models.ForeignKey(UserCollection, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
