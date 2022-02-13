from rest_framework import serializers
from . import models

# Price conversions from copper pieces to gold and silver pieces.
COPPER_TO_GOLD = 100
COPPER_TO_SILVER = 10


class AbilityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AbilityScore
        fields = ('id', 'abbreviated_name', 'name', 'description')


# class AbilityScoreSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     abbreviated_name = serializers.CharField(max_length=3)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField(allow_blank=True)


class DamageSerializer(serializers.Serializer):
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


class SkillSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    ability_score = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)


class WeaponSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    weapon_type = serializers.CharField(max_length=255)
    cost = serializers.SerializerMethodField(method_name='calculate_cost')
    damage = serializers.CharField(max_length=10, allow_null=True)
    damage_type = serializers.CharField(max_length=255)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True)
    properties = serializers.StringRelatedField(many=True)
    max_damage = serializers.SerializerMethodField(method_name='calculate_max_damage')

    def calculate_cost(self, weapon):
        """
        Return a string representation of the cost of each item in argument, rounded down to the nearest
        of gold (gp), silver(sp), or copper (cp) pieces.
        1 gold piece == 100 copper pieces.
        1 silver piece == 10 copper pieces.

        Args:
             weapon

        Returns:
            cost (str): Nicely formatted string representation of the item cost.
         """

        cost = '0'
        if int(weapon.cost) is None or int(weapon.cost) == 0:
            return cost

        cp, sp, gp = 0, 0, 0
        cost_in_copper = int(weapon.cost)
        while cost_in_copper >= COPPER_TO_GOLD:  # Convert copper to gold.
            gp += 1
            cost_in_copper -= COPPER_TO_GOLD
        while cost_in_copper >= COPPER_TO_SILVER:  # Convert copper to silver.
            sp += 1
            cost_in_copper -= COPPER_TO_SILVER
        cp = cost_in_copper  # Remainder is leftover cost in copper.

        cost = ''  # Remove 0 from string.
        if gp > 0:
            cost += str(gp) + 'gp, '
        if sp > 0:
            cost += str(sp) + 'sp, '
        if cp > 0:
            cost += str(cp) + 'cp '

        return cost.rstrip(' ,').lstrip()

    def calculate_max_damage(self, weapon):
        if weapon.damage:
            num_and_dice = str(weapon.damage).split('d')
            max_damage = int(num_and_dice[0]) * int(num_and_dice[1])
            return max_damage
        else:
            return 0


class WeaponPropertySerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)
