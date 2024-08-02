# Generated by Django 5.0.7 on 2024-08-04 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0008_alter_pokemon_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('L', 'Lagartija'), ('E', 'Eléctrico'), ('A', 'Agua'), ('P', 'Planta'), ('T', 'Tierra'), ('F', 'Fuego')], max_length=30),
        ),
    ]
