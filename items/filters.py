from django_filters.rest_framework import FilterSet

from .models import Equipment, Weapon


class EquipmentFilter(FilterSet):
    class Meta:
        model = Equipment
        fields = {
            'equipment_category': ['exact'],
            'cost': ['gt', 'lt'],
            'weight': ['gt', 'lt']
        }


class WeaponFilter(FilterSet):
    class Meta:
        model = Weapon
        fields = {
            'damage_type_id': ['exact'],
            'weapon_type_id': ['exact'],
            'properties': ['exact'],
            'cost': ['gt', 'lt'],
            'weight': ['gt', 'lt']
        }
