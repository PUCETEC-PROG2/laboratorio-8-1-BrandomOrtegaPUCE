# Generated by Django 5.0.7 on 2024-07-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0012_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('L', 'Lagartija'), ('P', 'Planta'), ('F', 'Fuego'), ('T', 'Tierra'), ('E', 'Electrico'), ('A', 'Agua')], max_length=30),
        ),
    ]
