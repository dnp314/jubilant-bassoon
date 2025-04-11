from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
# Create your models here.

def valid_resto_name_begin_with_a(value):
  if not value.startswith('a'):
    raise ValidationError("Yo whatsupp")


class Restaurant(models.Model):
  class TypeChoices(models.TextChoices):
    INDIAN = 'IN', 'Indian'
    CHINESE = 'CH', 'Chinese'
    ITALIAN = 'IT', 'Italian'
    OTHER = 'OT', 'Other'
  name = models.CharField(max_length=20)
  website = models.URLField(default='')
  date_opened = models.DateField()
  latitude = models.FloatField(
    validators=[MinValueValidator(-90), MaxValueValidator(90)]
  )
  longitude = models.FloatField(
    validators=[MinValueValidator(-180), MaxValueValidator(180)]
  )
  restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
  
  def __str__(self):
    return self.name

class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="ratings")
  rating = models.PositiveSmallIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)]
  )
  
  def __str__(self):
    return f"Rating: {self.rating}"
  
class Sale(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name="sales")
  income = models.DecimalField(max_digits=8, decimal_places=2)
  datetime = models.DateTimeField()