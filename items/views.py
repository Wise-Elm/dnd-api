from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers


@api_view(['GET', 'POST'])
def ability_score_list(request):
    if request.method == 'GET':
        queryset = models.AbilityScore.objects.all()
        serializer = serializers.AbilityScoreSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.AbilityScoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def ability_score_detail(request, id):
    ability_score = get_object_or_404(models.AbilityScore, pk=id)
    if request.method == 'GET':
        serializer = serializers.AbilityScoreSerializer(ability_score)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.AbilityScoreSerializer(ability_score, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def damage_type_list(request):
    if request.method == 'GET':
        queryset = models.DamageType.objects.all()
        serializer = serializers.DamageTypeSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.DamageTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def damage_type_detail(request, id):
    damage = get_object_or_404(models.DamageType, pk=id)
    if request.method == 'GET':
        serializer = serializers.DamageTypeSerializer(damage)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.DamageTypeSerializer(damage, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def equipment_list(request):
    if request.method == 'GET':
        queryset = models.Equipment.objects.select_related('equipment_category').all()
        serializer = serializers.EquipmentSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.EquipmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def equipment_detail(request, id):
    equipment = get_object_or_404(models.Equipment, pk=id)
    if request.method == 'GET':
        serializer = serializers.EquipmentSerializer(equipment)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.EquipmentSerializer(equipment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def equipment_category_list(request):
    if request.method == 'GET':
        queryset = models.EquipmentCategory.objects.all()
        serializer = serializers.EquipmentCategorySerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.EquipmentCategorySerializer(equipment_category_list, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def equipment_category_detail(request, id):
    equipment_category = get_object_or_404(models.EquipmentCategory, pk=id)
    if request.method == 'GET':
        serializer = serializers.EquipmentCategorySerializer(equipment_category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.EquipmentSerializer(equipment_category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def skill_list(request):
    if request.method == 'GET':
        queryset = models.Skill.objects.select_related('ability_score').all()
        serializer = serializers.SkillSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.SkillSerializer(skill_list, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def skill_detail(request, id):
    skill = get_object_or_404(models.Skill, pk=id)
    if request.method == 'GET':
        serializer = serializers.SkillSerializer(skill)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.EquipmentSerializer(skill_detail, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def weapon_list(request):
    if request.method == 'GET':
        queryset = models.Weapon.objects. \
            select_related('weapon_type', 'damage_type'). \
            prefetch_related('properties'). \
            all()
        serializer = serializers.WeaponSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.WeaponSerializer(weapon_list, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def weapon_detail(request, id):
    weapon = get_object_or_404(models.Weapon, pk=id)
    if request.method == 'GET':
        serializer = serializers.WeaponSerializer(weapon)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.EquipmentSerializer(weapon, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def weapon_property_list(request):
    if request.method == 'GET':
        queryset = models.WeaponProperty.objects.all()
        serializer = serializers.WeaponPropertySerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = serializers.WeaponPropertySerializer(weapon_property_list, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT'])
def weapon_property_detail(request, id):
    weapon_property = get_object_or_404(models.WeaponProperty, pk=id)
    if request.method == 'GET':
        serializer = serializers.WeaponPropertySerializer(weapon_property)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = serializers.EquipmentSerializer(weapon_property, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
