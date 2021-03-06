# Generated by Django 4.0.2 on 2022-02-14 00:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_weapon_properties_delete_weaponweaponproperty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='abilityscore',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='damagetype',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='equipmentcategory',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='weapon',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='weaponproperty',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='weapontype',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='weapon',
            name='properties',
            field=models.ManyToManyField(blank=True, to='items.WeaponProperty'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
