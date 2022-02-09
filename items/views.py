from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


@api_view()
def weapon_list(request):
    queryset = models.Weapon.objects. \
        select_related('weapon_type', 'damage_type'). \
        prefetch_related('properties'). \
        all()
    serializer = serializers.WeaponSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def weapon_detail(request, id):
    weapon = get_object_or_404(models.Weapon, pk=id)
    serializer = serializers.WeaponSerializer(weapon)
    return Response(serializer.data)


@api_view()
def ability_score_list(request):
    queryset = models.AbilityScore.objects.all()
    serializer = serializers.AbilityScoreSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def ability_score_detail(request, id):
    ability_score = get_object_or_404(models.AbilityScore, pk=id)
    serializer = serializers.AbilityScoreSerializer(ability_score)
    return Response(serializer.data)


@api_view()
def skill_list(request):
    queryset = models.Skill.objects.select_related('ability_score').all()
    serializer = serializers.SkillSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def skill_detail(request, id):
    skill = get_object_or_404(models.Skill, pk=id)
    serializer = serializers.SkillSerializer(skill)
    return Response(serializer.data)


@api_view()
def damage_type_list(request):
    queryset = models.DamageType.objects.all()
    serializer = serializers.DamageSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def damage_type_detail(request, id):
    damage = get_object_or_404(models.DamageType, pk=id)
    serializer = serializers.DamageSerializer(damage)
    return Response(serializer.data)


@api_view()
def weapon_property_list(request):
    queryset = models.WeaponProperty.objects.all()
    serializer = serializers.WeaponPropertySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def weapon_property_detail(request, id):
    weapon_property = get_object_or_404(models.WeaponProperty, pk=id)
    serializer = serializers.WeaponPropertySerializer(weapon_property)
    return Response(serializer.data)


@api_view()
def equipment_list(request):
    queryset = models.Equipment.objects.select_related('equipment_category').all()
    serializer = serializers.EquipmentSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def equipment_detail(request, id):
    equipment = get_object_or_404(models.Equipment, pk=id)
    serializer = serializers.EquipmentSerializer(equipment)
    return Response(serializer.data)


@api_view()
def equipment_category_list(request):
    queryset = models.EquipmentCategory.objects.all()
    serializer = serializers.EquipmentCategorySerializer(queryset, many=True)
    return Response(serializer.data)


@api_view()
def equipment_category_detail(request, id):
    equipment = get_object_or_404(models.EquipmentCategory, pk=id)
    serializer = serializers.EquipmentCategorySerializer(equipment)
    return Response(serializer.data)