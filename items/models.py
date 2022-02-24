from django.core.validators import MinValueValidator
from django.db import models


DEFAULT_ABBREVIATED_NAME_LEN = 3  # Character length.
DEFAULT_NAME_LEN = 255  # Character length.
DEFAULT_DAMAGE_MAX_CHARACTER_LEN = 10
DEFAULT_WEIGHT_MAX_DIGITS = 5  # ex. 111.11
DEFAULT_WEIGHT_DECIMAL_PLACES = 2  # ex. .11
DEFAULT_MIN_WEIGHT = 0  # May eventually have negative numbers with magic items.


class AbilityScore(models.Model):
    """
    Represents an Ability Score.

    Example:
        {
        'id': 1,
        'name': 'Charisma',
        'abbreviated_name': 'CHA',
        'description': 'Charisma measures your ability to ...',
        }
    """

    name = models.CharField(max_length=DEFAULT_NAME_LEN)
    abbreviated_name = models.CharField(max_length=DEFAULT_ABBREVIATED_NAME_LEN)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Skill(models.Model):
    """
    Represents a Skill.

    Example:
        {
        'id': 2,
        'name': 'Acrobatics',
        'ability_score': 3,
        'description': 'Your Dexterity (Acrobatics) check covers ...',
        }
    """

    name = models.CharField(max_length=DEFAULT_NAME_LEN)
    ability_score = models.ForeignKey(AbilityScore, models.PROTECT)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class WeaponType(models.Model):
    """
    Represents a Weapon Type.

    Example:
        {
        'id': 1,
        'name': 'Simple Ranged Weapons',
        }
    """

    name = models.CharField(max_length=DEFAULT_NAME_LEN)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class DamageType(models.Model):
    """
    Represents a Damage Type.

    Example:
        {
        'id': 1,
        'name': 'Acid',
        'description': 'The corrosive spray of a black dragon's ...',
        }
    """

    name = models.CharField(max_length=DEFAULT_NAME_LEN)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class WeaponProperty(models.Model):
    """
    Represents a Weapon Property.

    Example:
        {
        'id': 1,
        'name': 'Ammunition',
        'description': 'You can use a weapon that ...',
        }
    """

    name = models.CharField(max_length=DEFAULT_NAME_LEN)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Weapon(models.Model):
    """
    Represents a Weapon.

    Example:
        {
        'id': 24,
        'name': 'Battleaxe',
        'weapon_type': 3,
        'cost': 1000,
        'damage': '1d8',
        'damage_type': 12,
        'weight': 4.0,
        'properties': [
            11
        ]
        }
    """

    cost = models.PositiveIntegerField()
    damage = models.CharField(max_length=DEFAULT_DAMAGE_MAX_CHARACTER_LEN, null=True)
    damage_type = models.ForeignKey(DamageType, models.PROTECT)
    name = models.CharField(max_length=DEFAULT_NAME_LEN)
    properties = models.ManyToManyField(WeaponProperty, blank=True)
    weapon_type = models.ForeignKey(WeaponType, models.PROTECT)
    weight = models.DecimalField(
        max_digits=DEFAULT_WEIGHT_MAX_DIGITS,
        decimal_places=DEFAULT_WEIGHT_DECIMAL_PLACES,
        null=True,
        validators=[MinValueValidator(DEFAULT_MIN_WEIGHT)]
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class EquipmentCategory(models.Model):
    """
    Represents an Equipment Category.

    Example:
        {
        'id': 1,
        'name': 'Adventuring Gear',
        }
    """

    name = models.CharField(max_length=DEFAULT_NAME_LEN)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Equipment(models.Model):
    """
    Represents a piece of Equipment.

    Example:
        {
        'id': 1,
        'name': 'Abacus',
        'cost': 100,
        'equipment_category': 1,
        }
    """

    cost = models.PositiveIntegerField()
    equipment_category = models.ForeignKey(
        EquipmentCategory,
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=DEFAULT_NAME_LEN)
    weight = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
