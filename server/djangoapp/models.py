from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.PositiveIntegerField(validators=[MinValueValidator(1888), MaxValueValidator(2026)])

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('HATCHBACK', 'Hatchback'),
        ('UNIVERSAL', 'Universal')
    )
    type = models.CharField(max_length=15, choices=CAR_TYPES, default='SEDAN')
    year = models.PositiveIntegerField(default=2023, validators=[MinValueValidator(2000), MaxValueValidator(2025)])

    def __str__(self):
        return self.name