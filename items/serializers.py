from rest_framework import serializers
from . import models

# Price conversions from copper pieces to gold and silver pieces.
COPPER_TO_GOLD = 100  # Amount of copper in 1 gold piece.
COPPER_TO_SILVER = 10  # Amount of copper in 1 silver piece.


def format_cost(item):
    """Return a string representation of the cost of item in argument, rounded down to the nearest
    denomination of gold (gp), silver(sp), or copper (cp) pieces.
    1 gold piece == 100 copper pieces.
    1 silver piece == 10 copper pieces.

    Args:
         item(obj): item object with a cost attribute.

    Returns:
        cost (str): Nicely formatted string representation of the item cost.
     """

    if int(item.cost) is None or int(item.cost) == 0:
        cost = '0'
        return cost

    cp, sp, gp = 0, 0, 0
    cost_in_copper = int(item.cost)
    while cost_in_copper >= COPPER_TO_GOLD:  # Convert copper to gold.
        gp += 1
        cost_in_copper -= COPPER_TO_GOLD
    while cost_in_copper >= COPPER_TO_SILVER:  # Convert copper to silver.
        sp += 1
        cost_in_copper -= COPPER_TO_SILVER
    cp = cost_in_copper  # Remainder is leftover cost in copper.

    cost = ''
    if gp > 0:
        cost += str(gp) + 'gp, '
    if sp > 0:
        cost += str(sp) + 'sp, '
    if cp > 0:
        cost += str(cp) + 'cp '

    cost = cost.lstrip().rstrip(' ,')
    return cost


def format_weight(item):
    """Return item weight as a nicely readable string showing weight in pounds (lb).

    Args:
        item (object): Item object with weight a weight attribute.

    Returns:
        weight (str): Easily readable string showing weight in lb's.
    """

    weight = str(item.weight) + 'lb'
    return weight


class AbilityScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AbilityScore
        fields = ('id', 'abbreviated_name', 'name', 'description')


class DamageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DamageType
        fields = ('id', 'name', 'description')


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipment
        fields = ('id', 'name', 'cost', 'weight', 'equipment_category')

    # Convert cost from copper into denominations of gold, silver, and copper.
    cost = serializers.SerializerMethodField(method_name='_get_formatted_cost')
    equipment_category = serializers.StringRelatedField(many=False)
    weight = serializers.SerializerMethodField(method_name='_get_formatted_weight')

    def _get_formatted_cost(self, equipment: models.Equipment):
        """Return a nicely readable representation of item cost.

        Calls function format_cost().

        Args:
            equipment (obj): Equipment object.

        Returns:
            cost (str): String representation of equipment cost nicely formatted into proper denominations of gold,
                silver, and copper. ex: '1gp, 14sp, 2cp'.
        """

        cost = format_cost(equipment)
        return cost

    def _get_formatted_weight(self, equipment: models.Equipment):
        """Return a nicely readable representation of item weight.

        Calls function format_weight().

        Args:
            equipment (obj): Equipment object.

        Returns:
            weight (str): String representation of equipment weight nicely formatted.
        """

        weight = format_weight(equipment)
        return weight


class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EquipmentCategory
        fields = ('id', 'name')


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ('id', 'name', 'ability_score', 'description')


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Weapon
        fields = (
            'id',
            'name',
            'weapon_type',
            'cost',
            'damage',
            'max_damage',
            'damage_type',
            'weight',
            'properties'
        )

    cost = serializers.SerializerMethodField(method_name='get_formatted_cost')
    damage_type = serializers.StringRelatedField(many=False)
    max_damage = serializers.SerializerMethodField(method_name='get_max_damage')
    properties = serializers.StringRelatedField(many=True)
    weapon_type = serializers.StringRelatedField(many=False)
    weight = serializers.SerializerMethodField(method_name='get_formatted_weight')

    def get_formatted_cost(self, weapon: models.Weapon):
        """Return a nicely readable representation of weapon cost.

        Calls function format_cost().

        Args:
            weapon (obj): Weapon object.

        Returns:
            cost (str): String representation of weapon cost nicely formatted into proper denominations of gold,
                silver, and copper. ex: '1gp, 14sp, 2cp'.
        """
        cost = format_cost(weapon)
        return cost

    def get_formatted_weight(self, weapon: models.Weapon):
        """Return a nicely readable representation of item weight.

        Calls function format_weight().

        Args:
            weapon (obj): weapon object.

        Returns:
            weight (str): String representation of weapon weight nicely formatted.
        """

        weight = format_weight(weapon)
        return weight

    def get_max_damage(self, weapon: models.Weapon):
        """Return an integer representing the maximum possible damage allowable according to the weapons damage dice.

        Args:
            weapon (obj): Weapon object.

        Returns:
            max_damage (int): Integer representing the maximum allowable damage according to the weapons damage dice.
        """

        if weapon.damage:
            num_and_dice = str(weapon.damage).split('d')  # num_and_dice: list['number of dice', 'dice type']
            max_damage = int(num_and_dice[0]) * int(num_and_dice[1])
            return max_damage

        max_damage = 0
        return max_damage


class WeaponPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeaponProperty
        fields = ('id', 'name', 'description')
