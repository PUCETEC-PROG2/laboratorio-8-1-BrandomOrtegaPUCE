from django.db import models

class Trainer (models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)
    level = models.IntegerField(null=False, default=1)
    region = models.CharField(max_length=30, null=False)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Pokemon (models.Model):
    name = models.CharField(max_length=30, null=False)
    POKEMON_TYPES= {
        ('W', 'Water'),
        ('F', 'Fire'),
        ('N', 'Normal'),
        ('E', 'Electric'),
        ('G', 'Grass'),
        ('R', 'Rock'),
        ('I', 'Ice'),
        ('G', 'Ground')
    }
    type = models.CharField(max_length=15, choices=POKEMON_TYPES, null=False)
    weight = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    height = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='pokemon_images')
    
    def __str__(self) -> str:
        return self.name
    