# Generated by Django 5.0.7 on 2024-07-27 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0005_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('P', 'Planta'), ('L', 'Lagartija'), ('E', 'Electrico'), ('A', 'Agua'), ('T', 'Tierra'), ('F', 'Fuego')], max_length=30),
        ),
    ]