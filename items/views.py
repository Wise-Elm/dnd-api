from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class AbilityScoreList(APIView):
    """Display a list of Ability Scores based on items.models.AbilityScore.

    /items/ability/
    """

    def get(self, request):
        queryset = models.AbilityScore.objects.all()
        serializer = serializers.AbilityScoreSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.AbilityScoreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AbilityScoreDetail(APIView):
    def get(self, request, id):
        ability_score = get_object_or_404(models.AbilityScore, pk=id)
        serializer = serializers.AbilityScoreSerializer(ability_score)
        return Response(serializer.data)

    def put(self, request, id):
        ability_score = get_object_or_404(models.AbilityScore, pk=id)
        serializer = serializers.AbilityScoreSerializer(ability_score, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        ability_score = get_object_or_404(models.AbilityScore, pk=id)
        ability_score.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DamageTypeList(APIView):
    def get(self, request):
        queryset = models.DamageType.objects.annotate(
            weapon_count=Count('weapon')).\
            all()
        serializer = serializers.DamageTypeSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.DamageTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DamageTypeDetail(APIView):
    def get(self, request, id):
        damage = get_object_or_404(models.DamageType.objects.annotate(weapon_count=Count('weapon')), pk=id)
        serializer = serializers.DamageTypeSerializer(damage)
        return Response(serializer.data)

    def put(self, request, id):
        damage = get_object_or_404(models.DamageType.objects.annotate(weapon_count=Count('weapon')), pk=id)
        serializer = serializers.DamageTypeSerializer(damage, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        damage = get_object_or_404(models.DamageType.objects.annotate(weapon_count=Count('weapon')), pk=id)
        damage.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipmentList(APIView):
    def get(self, request):
        queryset = models.Equipment.objects.select_related('equipment_category').all()
        serializer = serializers.EquipmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.EquipmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EquipmentDetail(APIView):
    def get(self, request, id):
        equipment = get_object_or_404(models.Equipment, pk=id)
        serializer = serializers.EquipmentSerializer(equipment)
        return Response(serializer.data)

    def put(self, request, id):
        equipment = get_object_or_404(models.Equipment, pk=id)
        serializer = serializers.EquipmentSerializer(equipment, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        equipment = get_object_or_404(models.Equipment, pk=id)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EquipmentCategoryList(APIView):
    def get(self, request):
        queryset = models.EquipmentCategory.objects.all()
        serializer = serializers.EquipmentCategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.EquipmentCategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EquipmentCategoryDetail(APIView):
    def get(self, request, id):
        equipment_category = get_object_or_404(models.EquipmentCategory, pk=id)
        serializer = serializers.EquipmentCategorySerializer(equipment_category)
        return Response(serializer.data)

    def put(self, request, id):
        equipment_category = get_object_or_404(models.EquipmentCategory, pk=id)
        serializer = serializers.EquipmentSerializer(equipment_category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        equipment_category = get_object_or_404(models.EquipmentCategory, pk=id)
        equipment_category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillList(APIView):
    def get(self, request):
        queryset = models.Skill.objects.select_related('ability_score').all()
        serializer = serializers.SkillSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SkillSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SkillDetail(APIView):
    def get(self, request, id):
        skill = get_object_or_404(models.Skill, pk=id)
        serializer = serializers.SkillSerializer(skill)
        return Response(serializer.data)

    def put(self, request, id):
        skill = get_object_or_404(models.Skill, pk=id)
        serializer = serializers.SkillSerializer(skill, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        skill = get_object_or_404(models.Skill, pk=id)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WeaponList(APIView):
    def get(self, request):
        queryset = models.Weapon.objects.\
            select_related('weapon_type', 'damage_type').\
            prefetch_related('properties').\
            all()
        serializer = serializers.WeaponSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.WeaponSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WeaponDetail(APIView):
    def get(self, request, id):
        weapon = get_object_or_404(models.Weapon, pk=id)
        serializer = serializers.WeaponSerializer(weapon)
        return Response(serializer.data)

    def put(self, request, id):
        weapon = get_object_or_404(models.Weapon, pk=id)
        serializer = serializers.WeaponSerializer(weapon, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        weapon = get_object_or_404(models.Weapon, pk=id)
        weapon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WeaponPropertyList(APIView):
    def get(self, request):
        queryset = models.WeaponProperty.objects.all()
        serializer = serializers.WeaponPropertySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.WeaponPropertySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class WeaponPropertyDetail(APIView):
    def get(self, request, id):
        weapon_property = get_object_or_404(models.WeaponProperty, pk=id)
        serializer = serializers.WeaponPropertySerializer(weapon_property)
        return Response(serializer.data)

    def put(self, request, id):
        weapon_property = get_object_or_404(models.WeaponProperty, pk=id)
        serializer = serializers.WeaponPropertySerializer(weapon_property, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        weapon_property = get_object_or_404(models.WeaponProperty, pk=id)
        weapon_property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
