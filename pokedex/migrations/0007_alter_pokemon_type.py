# Generated by Django 5.0.7 on 2024-07-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0006_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('E', 'Electrico'), ('A', 'Agua'), ('L', 'Lagartija'), ('F', 'Fuego'), ('T', 'Tierra')], max_length=30),
        ),
    ]
