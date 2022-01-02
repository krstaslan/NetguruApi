from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Car(models.Model):
    make = models.TextField(max_length=50, unique=False)
    model = models.TextField(max_length=50, unique=True)
    avg_rating= models.FloatField(default=5, null=False)


class Rating(models.Model):
    car_id =models.ForeignKey(Car, on_delete=models.CASCADE, default="")
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)], null=False)
    #rates_number=models.FloatField(default=0, null=False)
    class Meta:
        verbose_name_plural=''

    def get_rating(self):
        return self.rating

# I will add sum of rates in views
class Popular(models.Model):
    make = models.ForeignKey(Rating, on_delete=models.CASCADE)


    def __str__(self):
        return self.car_id

'''
class Popular(models.Model):
    car_rating=models.ForeignKey(Rating,on_delete=models.CASCADE)

'''
'''
# ı want to calculate avarage every time to make it updated.
#I will do it in views
class AvarageRating(models.Model):
    make=models.ForeignKey(Car, on_delete=models.CASCADE)
    avg_rating = models.FloatField(default=1)
'''