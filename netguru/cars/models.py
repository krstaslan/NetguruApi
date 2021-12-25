from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Car(models.Model):
    make = models.TextField(max_length=20, unique=False)
    model = models.TextField(max_length=20, unique=True)
    avg_rating = models.FloatField(default=1)

    def __str__(self):
        return self.make

class Rating(models.Model):
    id =models.ForeignKey(Car,on_delete=models.CASCADE,primary_key=True)
    rating = models.FloatField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)], null=False)

    def __str__(self):
        return self.id
'''
class Popular(models.Model):
    id = models.ForeignKey(Car, on_delete=models.CASCADE, primary_key=True)
    make =models.ForeignKey(Car, on_delete=models.CASCADE)
    model =models.ForeignKey(Car, on_delete=models.CASCADE)
    rates_number = models.FloatField(default=1)

    def __str__(self):
        return self.id
'''