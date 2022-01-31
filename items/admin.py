from django.contrib import admin
from . models import AbilityScore, Equipment, EquipmentCategory, Skill, WeaponProperty, Weapon, DamageType, \
    WeaponType, WeaponWeaponProperty


admin.site.register(AbilityScore)
admin.site.register(Equipment)
admin.site.register(EquipmentCategory)
admin.site.register(Skill)
admin.site.register(WeaponProperty)
admin.site.register(Weapon)
admin.site.register(DamageType)
admin.site.register(WeaponType)
admin.site.register(WeaponWeaponProperty)

