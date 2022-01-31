# Generated by Django 4.0.1 on 2022-01-31 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DamageType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='abilityscore',
            old_name='Abbreviated_name',
            new_name='abbreviated_name',
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.PositiveIntegerField()),
                ('damage', models.CharField(max_length=10)),
                ('damage_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.damagetype')),
                ('weapon_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='items.weapontype')),
            ],
        ),
        migrations.CreateModel(
            name='WeaponWeaponProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.weaponproperty')),
                ('weapon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.weapon')),
            ],
            options={
                'unique_together': {('weapon_id', 'property_id')},
            },
        ),
    ]
