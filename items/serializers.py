from rest_framework import serializers


class WeaponSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    weapon_type = serializers.CharField(max_length=255)
    cost = serializers.IntegerField()
    damage = serializers.CharField(max_length=10, allow_null=True)
    damage_type = serializers.CharField(max_length=255)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True)
    properties = serializers.StringRelatedField(many=True)
    max_damage = serializers.SerializerMethodField(method_name='calculate_max_damage')

    def calculate_max_damage(self, weapon):
        return 'test'


class AbilityScoreSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    abbreviated_name = serializers.CharField(max_length=3)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)


class SkillSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    ability_score = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)


class DamageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)


class WeaponPropertySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)


class EquipmentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    cost = serializers.IntegerField()
    equipment_category = serializers.CharField(max_length=255)


class EquipmentCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
