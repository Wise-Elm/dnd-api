from rest_framework import serializers
from . models import Skill, WeaponProperty


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'ability_score', 'description')


class WeaponPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeaponProperty
        fields = ('id', 'name', 'description')