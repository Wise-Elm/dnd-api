from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from . import models


@admin.register(models.AbilityScore)
class AbilityScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviated_name']
    ordering = ['name', 'abbreviated_name']
    list_per_page = 40


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'equipment_category']
    ordering = ['name', 'cost', 'equipment_category']
    list_per_page = 40


@admin.register(models.EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    list_per_page = 40


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'ability_score', 'description']
    ordering = ['name', 'ability_score']
    list_per_page = 40


@admin.register(models.WeaponProperty)
class WeaponPropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['name']
    list_per_page = 40


@admin.register(models.Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'weapon_type',
        'damage',
        'max_damage',
        'damage_type',
        'cost',
        'weight',
        'property_count'
    ]
    ordering = ['name']
    list_per_page = 40

    @admin.display()
    def max_damage(self, weapon):
        if weapon.damage is not None:
            max_damage = int(weapon.damage[0]) * int(weapon.damage[2:])
            return int(max_damage)
        else:
            return 0

    @admin.display(ordering='property_count')
    def property_count(self, weapon):
        return weapon.property_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            property_count=Count('properties')
        )

    # @admin.display()
    # def weapon_type(self, weapon):
    #     url = reverse('admin:items_weapontype_changelist')
    #     return format_html('<a href="http://google.com">{}</a>', weapon_type)


@admin.register(models.DamageType)
class DamageTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    ordering = ['name']
    list_per_page = 40


@admin.register(models.WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'weapon_count']
    ordering = ['name']
    list_per_page = 40

    @admin.display(ordering='weapon_count')
    def weapon_count(self, weapontype):
        return weapontype.weapon_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            weapon_count=Count('weapon')
        )


# admin.site.register(models.AbilityScore)
# admin.site.register(models.Equipment)
# admin.site.register(models.EquipmentCategory)
# admin.site.register(models.Skill)
# admin.site.register(models.WeaponProperty)
# admin.site.register(models.Weapon)
# admin.site.register(models.DamageType)
# admin.site.register(models.WeaponType)

