# Generated by Django 4.0.1 on 2022-01-31 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_alter_weapon_damage'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]