from rest_framework import serializers

from .models import AbilityScore, DamageType, Equipment, EquipmentCategory, \
    Skill, Weapon, WeaponProperty, WeaponType

# Price conversions from copper pieces to gold and silver pieces.
COPPER_TO_GOLD = 100  # Amount of copper in 1 gold piece.
COPPER_TO_SILVER = 10  # Amount of copper in 1 silver piece.


def format_cost_for_storage(item):
    """
    Return an integer representation of the cost of item in argument.
    1 gold piece == 100 copper pieces.
    1 silver piece == 10 copper pieces.

    Args:
         item (obj): item object with a cost attribute.

    Returns:
        cost (int): Integer representation of the item cost.
     """

    # Return if item.cost is integer. Input is already in cp format.
    if item.cost is int:
        cost = item.cost
        return cost

    # Return - skip calculations - when items.cost is 0.
    if item.cost == '0':
        cost = int(item.cost)
        return cost

    # Split item.cost into denominations of gp, sp, and cp.
    cp, sp, gp = 0, 0, 0
    cost_in_all = item.cost.split()
    for denomination in cost_in_all:
        if 'gp' in denomination:
            index_ = denomination.index('gp')
            gp = int(denomination[:index_])
        elif 'sp' in denomination:
            index_ = denomination.index('sp')
            sp = int(denomination[:index_])
        elif 'cp' in denomination:
            index_ = denomination.index('cp')
            cp = int(denomination[:index_])

    # Convert and sum all denominations together into cp.
    if gp > 0:
        cp += gp * COPPER_TO_GOLD
    if sp > 0:
        cp += sp * COPPER_TO_SILVER
    cost = cp

    return cost


def format_cost_for_user(item):
    """
    Return a string representation of the cost of item in argument, rounded
    down to the nearest denomination of gold (gp), silver(sp), or copper (cp)
    pieces.
    1 gold piece == 100 copper pieces.
    1 silver piece == 10 copper pieces.

    Args:
         item (obj): item object with a cost attribute.

    Returns:
        cost (str): Nicely formatted string representation of the item cost.
     """

    # Return 0 when no conversion is needed.
    if int(item.cost) is None or int(item.cost) == 0:
        cost = '0'
        return cost

    # Covert cp into sp and gp. (Rather than 1001cp, --> cp, sp, gp = 1, 0, 10)
    cp, sp, gp = 0, 0, 0
    cost_in_copper = int(item.cost)
    while cost_in_copper >= COPPER_TO_GOLD:  # Convert copper to gold.
        gp += 1
        cost_in_copper -= COPPER_TO_GOLD
    while cost_in_copper >= COPPER_TO_SILVER:  # Convert copper to silver.
        sp += 1
        cost_in_copper -= COPPER_TO_SILVER
    cp = cost_in_copper  # Remainder is leftover cost in copper.

    # Create nicely formatted string for user.
    # cp, sp, gp = 1, 0, 10 --> cost = '10gp, 1cp'
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
    """
    Return item weight as a nicely readable string showing weight in pounds
    (lb).

    Args:
        item (object): Item object with weight a weight attribute.

    Returns:
        weight (str): Easily readable string showing weight in lb's.
    """

    weight = str(item.weight) + 'lb'
    return weight


class AbilityScoreSerializer(serializers.ModelSerializer):
    """
    Serialize models.AbilityScore.

    Example:
        {
        "id": 1,
        "abbreviated_name": "CHA",
        "name": "Charisma",
        "description": "Charisma measures your ability to interact ...",
        }
    """

    class Meta:
        model = AbilityScore
        fields = ('id', 'abbreviated_name', 'name', 'description')


class DamageTypeSerializer(serializers.ModelSerializer):
    """
    Serialize models.DamageType.

    Example:
        {
        "id": 1,
        "name": "Acid",
        "weapon_count": 0,
        "description": "The corrosive spray of a black dragon's breath ...",
        }
    """

    weapon_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = DamageType
        fields = ('id', 'name', 'weapon_count', 'description')
        w = serializers.IntegerField(read_only=True)


class EquipmentSerializer(serializers.ModelSerializer):
    """
    Serialize models.Equipment.

    Example:
        {
        "id": 1,
        "name": "Abacus",
        "cost": 200,
        "formatted_cost": "2gp",
        "weight": 2,
        "formatted_weight": "2lb",
        "equipment_category": 1,
        }
    """

    formatted_cost = serializers.SerializerMethodField(
        method_name='get_formatted_cost')
    formatted_weight = serializers.SerializerMethodField(
        method_name='get_formatted_weight')

    class Meta:
        model = Equipment
        fields = (
            'id',
            'name',
            'cost',
            'formatted_cost',
            'weight',
            'formatted_weight',
            'equipment_category',
        )

    def get_formatted_cost(self, equipment: Equipment):
        """
        Return a nicely readable representation of item cost.

        Calls function format_cost().

        Args:
            equipment (obj): Equipment object.

        Returns:
            cost (str): String representation of equipment cost nicely
                formatted into proper denominations of gold, silver, and
                copper. ex: '1gp, 14sp, 2cp'.
        """

        cost = format_cost_for_user(equipment)
        return cost

    def get_formatted_weight(self, equipment: Equipment):
        """
        Return a nicely readable representation of item weight.

        Calls function format_weight().

        Args:
            equipment (obj): Equipment object.

        Returns:
            weight (str): String representation of equipment weight nicely
            formatted.
        """

        weight = format_weight(equipment)
        return weight


class EquipmentCategorySerializer(serializers.ModelSerializer):
    """
    Serialize models.EquipmentCategory.

    Example:
        {
        "id": 1,
        "name": "Adventuring Gear",,
        }
    """

    class Meta:
        model = EquipmentCategory
        fields = ('id', 'name')


class SkillSerializer(serializers.ModelSerializer):
    """
    Serialize models.Skill.

    Example:
        {
        "id": 2,
        "name": "Acrobatics",
        "ability_score": 3,
        "description": "Your Dexterity (Acrobatics) check covers your ...",
        }
    """

    class Meta:
        model = Skill
        fields = ('id', 'name', 'ability_score', 'description')


class WeaponTypeSerializer(serializers.ModelSerializer):
    """
    Serialize models.WeaponType.

    Example:
        {
        "id": 3,
        "name": "Martial Melee Weapons",
        }
    """

    class Meta:
        model = WeaponType
        fields = ('id', 'name')


class WeaponPropertySerializer(serializers.ModelSerializer):
    """
    Serialize models.WeaponProperty.

    Example:
        {
        "id": 1,
        "name": "Ammunition",
        "description": "You can use a weapon that has the ...",
        }
    """

    class Meta:
        model = WeaponProperty
        fields = ('id', 'name', 'description')


class WeaponSerializer(serializers.ModelSerializer):
    """
    Serialize models.Weapon.

    Example:
        {
            "id": 24,
            "name": "Battleaxe",
            "weapon_type": {
                "id": 3,
                "name": "Martial Melee Weapons"
            },
            "cost": 1000,
            "formatted_cost": "10gp",
            "damage": "1d8",
            "max_damage": 8,
            "damage_type": {
                "id": 12,
                "name": "Slashing",
                "description": "Swords, axes, and monsters' claws deal
                slashing damage."
            },
            "weight": 4.0,
            "formatted_weight": "4.00lb",
            "properties": [
                11
            ]
        }
    """

    formatted_cost = serializers.SerializerMethodField(
        method_name='get_formatted_cost')
    max_damage = serializers.SerializerMethodField(
        method_name='get_max_damage')
    formatted_weight = serializers.SerializerMethodField(
        method_name='get_formatted_weight')
    damage_type = DamageTypeSerializer()  # Display DamageType object not just id.
    weapon_type = WeaponTypeSerializer()

    class Meta:
        model = Weapon
        fields = (
            'id',
            'name',
            'weapon_type',
            'cost',
            'formatted_cost',
            'damage',
            'max_damage',
            'damage_type',
            'weight',
            'formatted_weight',
            'properties',
        )

    def get_formatted_cost(self, weapon):
        """
        Return a nicely readable representation of weapon cost.

        Calls function format_cost().

        Args:
            weapon (obj): Weapon object.

        Returns:
            cost (str): String representation of weapon cost nicely formatted
                into proper denominations of gold, silver, and copper. ex:
                '1gp, 14sp, 2cp'.
        """

        cost = format_cost_for_user(weapon)
        return cost

    def get_formatted_weight(self, weapon):
        """
        Return a nicely readable representation of item weight.

        Calls function format_weight().

        Args:
            weapon (obj): weapon object.

        Returns:
            weight (str): String representation of weapon weight nicely
            formatted.
        """

        weight = format_weight(weapon)
        return weight

    def get_max_damage(self, weapon):
        """
        Return an integer representing the maximum possible damage allowable
        according to the weapons damage dice.

        Args:
            weapon (obj): Weapon object.

        Returns:
            max_damage (int): Integer representing the maximum allowable damage
                according to the weapons damage dice.
        """

        if weapon.damage:
            # num_and_dice: list['number of dice', 'dice type']
            num_and_dice = str(weapon.damage).split('d')
            max_damage = int(num_and_dice[0]) * int(num_and_dice[1])
            return max_damage

        max_damage = 0
        return max_damage
