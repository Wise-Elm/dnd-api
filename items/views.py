from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class AbilityScoreList(ListCreateAPIView):
    """Display a list of Ability Score objects based on models.AbilityScore.

    /items/ability/
    """

    queryset = models.AbilityScore.objects.all()
    serializer_class = serializers.AbilityScoreSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class AbilityScoreDetail(RetrieveUpdateDestroyAPIView):
    """Display a Ability Score object corresponding to associated id, based on models.AbilityScore.

    /items/ability/id
    """

    queryset = models.AbilityScore.objects.all()
    serializer_class = serializers.AbilityScoreSerializer


class DamageTypeList(ListCreateAPIView):
    """Display a list of DamageType objects based on models.DamageType

    /items/damage/
    """

    queryset = models.DamageType.objects.annotate(weapon_count=Count('weapon')).all()
    serializer_class = serializers.DamageTypeSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class DamageTypeDetail(RetrieveUpdateDestroyAPIView):
    """Display a DamageType object corresponding to associated id, based on models.DamageType.

    /items/damage/id
    """

    queryset = models.DamageType.objects.all()
    serializer_class = serializers.DamageTypeSerializer


class EquipmentList(ListCreateAPIView):
    """Display a list of Equipment objects based on models.Equipment

    /items/equipment/
    """

    queryset = models.Equipment.objects.select_related('equipment_category').all()
    serializer_class = serializers.EquipmentSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EquipmentDetail(RetrieveUpdateDestroyAPIView):
    """Display a Equipment object corresponding to associated id, based on models.Equipment.

    /items/equipment/id
    """

    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer


class EquipmentCategoryList(ListCreateAPIView):
    """Display a list of EquipmentCategory objects based on models.EquipmentCategory

    /items/equipment-category/
    """

    queryset = models.EquipmentCategory.objects.all()
    serializer_class = serializers.EquipmentCategorySerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EquipmentCategoryDetail(RetrieveUpdateDestroyAPIView):
    """Display a EquipmentCategory object corresponding to associated id, based on models.EquipmentCategory.

    /items/equipment-category/id
    """

    queryset = models.EquipmentCategory.objects.all()
    serializer_class = serializers.EquipmentCategorySerializer


class SkillList(ListCreateAPIView):
    """Display a list of Skill objects based on models.Skill

    /items/skill/
    """

    queryset = models.Skill.objects.select_related('ability_score').all()
    serializer_class = serializers.SkillSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class SkillDetail(RetrieveUpdateDestroyAPIView):
    """Display a Skill object corresponding to associated id, based on models.skill.

    /items/skill/id
    """

    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer


class WeaponList(ListCreateAPIView):
    """Display a list of Weapon objects based on models.Weapon

    /items/weapon/
    """

    queryset = models.Weapon.objects.\
        select_related('weapon_type', 'damage_type').\
        prefetch_related('properties').\
        all()
    serializer_class = serializers.WeaponSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class WeaponDetail(RetrieveUpdateDestroyAPIView):
    """Display a Weapon object corresponding to associated id, based on models.Weapon.

    /items/weapon/id
    """

    queryset = models.Weapon.objects.all()
    serializer_class = serializers.WeaponSerializer


class WeaponPropertyList(ListCreateAPIView):
    """Display a list of WeaponProperty objects based on models.WeaponProperty

    /items/weapon-property/
    """

    queryset = models.WeaponProperty.objects.all()
    serializer_class = serializers.WeaponPropertySerializer

    def get_serializer_context(self):
        return {'request': self.request}


class WeaponPropertyDetail(RetrieveUpdateDestroyAPIView):
    """Display a WeaponProperty object corresponding to associated id, based on models.WeaponProperty.

    /items/weapon-property/id
    """

    queryset = models.WeaponProperty.objects.all()
    serializer_class = serializers.WeaponPropertySerializer
