from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode

from . import models


@admin.register(models.AbilityScore)
class AbilityScoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviated_name']
    list_per_page = 40
    ordering = ['name', 'abbreviated_name']
    search_fields = ['name']


@admin.register(models.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'equipment_category']
    list_per_page = 40
    ordering = ['name', 'cost', 'equipment_category']
    search_fields = ['name']


@admin.register(models.EquipmentCategory)
class EquipmentCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 40
    ordering = ['name']
    search_fields = ['name']


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'ability_score', 'description']
    list_per_page = 40
    ordering = ['name', 'ability_score']
    search_fields = ['name']


@admin.register(models.WeaponProperty)
class WeaponPropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'weapon_count', 'description']
    list_per_page = 40
    ordering = ['name']
    search_fields = ['name']


    @admin.display(ordering='weapon_count')
    def weapon_count(self, weaponproperty):
        url = (
            reverse('admin:items_weapon_changelist')
            + '?'
            + urlencode({
                'properties__id': str(weaponproperty.id)
            }))

        return format_html('<a href="{}">{}</a>', url, weaponproperty.weapon_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            weapon_count=Count('weapon')
        )


@admin.register(models.Weapon)
class WeaponAdmin(admin.ModelAdmin):
    autocomplete_fields = ['weapon_type', 'damage_type']
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
    list_filter = ['weapon_type', 'properties', 'damage_type']
    list_per_page = 40
    ordering = ['name']
    search_fields = ['name']

    @admin.display()
    def max_damage(self, weapon):
        if weapon.damage is not None:
            max_damage = int(weapon.damage[0]) * int(weapon.damage[2:])
            return max_damage
        else:
            return 0

    @admin.display(ordering='property_count')
    def property_count(self, weapon):
        return weapon.property_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            property_count=Count('properties')
        )


@admin.register(models.DamageType)
class DamageTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'weapon_count', 'description']
    list_per_page = 40
    ordering = ['name']
    search_fields = ['name']

    @admin.display(ordering='weapon_count')
    def weapon_count(self, damagetype):
        url = (
            reverse('admin:items_weapon_changelist')
            + '?'
            + urlencode({
                'damage_type__id': str(damagetype.id)
            }))
        return format_html('<a href="{}">{}</a>', url, damagetype.weapon_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            weapon_count=Count('weapon')
        )


@admin.register(models.WeaponType)
class WeaponTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'weapon_count']
    list_per_page = 40
    ordering = ['name']
    search_fields = ['name']

    @admin.display(ordering='weapon_count')
    def weapon_count(self, weapontype):
        url = (
            reverse('admin:items_weapon_changelist')
            + '?'
            + urlencode({
                'weapon_type__id': str(weapontype.id)
            }))
        return format_html('<a href="{}">{}</a>', url, weapontype.weapon_count)

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

