# Generated by Django 5.0.7 on 2024-07-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('L', 'Lagartija'), ('A', 'Agua'), ('E', 'Electrico'), ('F', 'Fuego'), ('P', 'Planta')], max_length=30),
        ),
    ]
