# Generated by Django 5.0.7 on 2024-07-27 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0013_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('L', 'Lagartija'), ('P', 'Planta'), ('T', 'Tierra'), ('A', 'Agua'), ('E', 'Electrico'), ('F', 'Fuego')], max_length=30),
        ),
    ]