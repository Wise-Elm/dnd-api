from django.db.models import Count
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *


class AbilityScoreViewSet(ModelViewSet):
    """
    Display a single AbilityScore object if id is provided, otherwise
    display a list of AbilityScore objects based on models.AbilityScore.
        Example:
            Returns list of AbilityScore objects:
                /items/ability/
            Returns single AbilityScore object based on id:
                /items/ability/id
    """

    queryset = AbilityScore.objects.all()
    serializer_class = AbilityScoreSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class DamageTypeViewSet(ModelViewSet):
    """
    Display a single DamageType object if id is provided, otherwise display
    a list of DamageType objects based on models.DamageType.
        Example:
            Returns list of DamageType objects:
                /items/damage/
            Returns single DamageType object based on id:
                /items/damage/id
    """

    queryset = DamageType.objects.annotate(weapon_count=Count('weapon')).all()
    serializer_class = DamageTypeSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EquipmentViewSet(ModelViewSet):
    """
    Display a single Equipment object if id is provided, otherwise display
    a list of Equipment objects based on models.Equipment.
        Example:
            Returns list of Equipment objects:
                /items/equipment/
            Returns single Equipment object based on id:
                /items/equipment/id

    Filter Equipment objects by Equipment Category by appending
    /?equipment_category=id.
        Example:
        /items/equipment/?equipment_category=id
    """

    serializer_class = EquipmentSerializer

    def get_queryset(self):
        queryset = Equipment.objects.all()
        category_id = self.request.query_params.get('equipment_category')
        if category_id is not None:
            queryset = queryset.filter(equipment_category_id=category_id)
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}


class EquipmentCategoryViewSet(ModelViewSet):
    """
    Display a single EquipmentCategory object if id is provided, otherwise
    display a list of EquipmentCategory objects based on
    models.EquipmentCategory.
        Example:
            Returns list of EquipmentCategory objects:
                /items/equipment-category
            Returns single EquipmentCategory object based on id:
                /items/equipment-category/id
    """

    queryset = EquipmentCategory.objects.all()
    serializer_class = EquipmentCategorySerializer

    def get_serializer_context(self):
        return {'request': self.request}


class SkillViewSet(ModelViewSet):
    """
    Display a single Skill object if id is provided, otherwise display a
    list of skill objects based on models.skill.
        Example:
            /items/skill/   Returns list of Skill objects.
            /items/skill/id     Returns single Skill object based on id.

    Filter Skill objects by Ability Score by appending /?ability_score=id.
        Example:
            /items/skill/?ability_score=id
    """

    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = Skill.objects.all()
        ability_score_id = self.request.query_params.get('ability_score')
        if ability_score_id is not None:
            queryset = queryset.filter(ability_score_id=ability_score_id)
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}


class WeaponViewSet(ModelViewSet):
    """
    Display a single Weapon object if id is provided, otherwise display a
    list of Weapon objects based on models.Weapon.
    Example:
        Returns list of Weapon objects:
            /items/weapon/
        Return single Weapon object based on id:
            /items/weapon/id

    Filter Weapon objects by Weapon Type by appending /?weapon_type=id.
        Example:
            /items/weapon/?weapon_type=id

    Filter Weapon objects by Damage Type by appending /?damage_type=id.
        Example:
            /items/weapon/?damage_type=id

    Filter Weapon objects by Weapon Property Type by appending
    /?property_type=id.
        Example:
            /items/weapon/?damage_type=id
    """

    serializer_class = WeaponSerializer

    def get_queryset(self):
        queryset = Weapon.objects.all()
        weapon_type_id = self.request.query_params.get('weapon_type')
        damage_type_id = self.request.query_params.get('damage_type')
        property_type_id = self.request.query_params.get('property_type')
        if weapon_type_id is not None:
            queryset = queryset.filter(weapon_type_id=weapon_type_id)
            return queryset
        elif damage_type_id is not None:
            queryset = queryset.filter(damage_type_id=damage_type_id)
            return queryset
        elif property_type_id is not None:
            queryset = queryset.filter(properties=property_type_id)
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}


class WeaponPropertyViewSet(ModelViewSet):
    """
    Display a single WeaponProperty object if id is provided, otherwise
    display a list of WeaponProperty objects based on models.WeaponProperty.
        Example:
            Returns list of WeaponProperty objects:
                /items/weapon-property
            Returns a WeaponProperty object based on id.
                /items/weapon-property/id
    """

    queryset = WeaponProperty.objects.all()
    serializer_class = WeaponPropertySerializer

    def get_serializer_context(self):
        return {'request': self.request}
