# Generated by Django 5.0.7 on 2024-07-27 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0010_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('T', 'Tierra'), ('F', 'Fuego'), ('E', 'Electrico'), ('L', 'Lagartija'), ('P', 'Planta'), ('A', 'Agua')], max_length=30),
        ),
    ]
