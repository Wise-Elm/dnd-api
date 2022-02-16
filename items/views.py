from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class AbilityScoreViewSet(ModelViewSet):
    """Display a single AbilityScore object if id is provided, otherwise display a list of AbilityScore objects based
    on models.AbilityScore.

    /items/ability/id
    """

    queryset = models.AbilityScore.objects.all()
    serializer_class = serializers.AbilityScoreSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class DamageTypeViewSet(ModelViewSet):
    """Display a single DamageType object if id is provided, otherwise display a list of DamageType objects based
    on models.DamageType.

    /items/damage/id
    """

    queryset = models.DamageType.objects.annotate(weapon_count=Count('weapon')).all()
    serializer_class = serializers.DamageTypeSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EquipmentViewSet(ModelViewSet):
    """Display a single Equipment object if id is provided, otherwise display a list of Equipment objects based
    on models.Equipment.

    /items/equipment/id
    """

    queryset = models.Equipment.objects.all()
    serializer_class = serializers.EquipmentSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class EquipmentCategoryViewSet(ModelViewSet):
    """Display a single EquipmentCategory object if id is provided, otherwise display a list of EquipmentCategory
    objects based on models.EquipmentCategory.

    /items/equipment-category/id
    """

    queryset = models.EquipmentCategory.objects.all()
    serializer_class = serializers.EquipmentCategorySerializer

    def get_serializer_context(self):
        return {'request': self.request}


class SkillViewSet(ModelViewSet):
    """Display a single Skill object if id is provided, otherwise display a list of skill objects based on
    models.skill.

    /items/skill/id
    """

    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class WeaponViewSet(ModelViewSet):
    """Display a single Weapon object if id is provided, otherwise display a list of Weapon objects based on
    models.Weapon.

    /items/weapon/id
    """

    queryset = models.Weapon.objects.all()
    serializer_class = serializers.WeaponSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class WeaponPropertyViewSet(ModelViewSet):
    """Display a single WeaponProperty object if id is provided, otherwise display a list of WeaponProperty objects
    based on models.WeaponProperty.

    /items/weapon-property/id
    """

    queryset = models.WeaponProperty.objects.all()
    serializer_class = serializers.WeaponPropertySerializer

    def get_serializer_context(self):
        return {'request': self.request}
