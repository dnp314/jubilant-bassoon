from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Restaurant(models.Model):
  class TypeChoices(models.TextChoices):
    INDIAN = 'IN', 'Indian'
    CHINESE = 'CH', 'Chinese'
    ITALIAN = 'IT', 'Italian'
    OTHER = 'OT', 'Other'
  name = models.CharField(max_length=20)
  website = models.URLField(default='')
  date_opened = models.DateField()
  latitude = models.FloatField()
  longitude = models.FloatField()
  restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)
  
  def __str__(self):
    return self.name

class Rating(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
  rating = models.PositiveSmallIntegerField()
  
  def __str__(self):
    return f"Rating: {self.rating}"
  
class Sale(models.Model):
  restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True)
  income = models.DecimalField(max_digits=8, decimal_places=2)
  datetime = models.DateTimeField()