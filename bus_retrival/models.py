from django.db import models
from datetime import datetime  
class Mechanical(models.Model):
    registerNo = models.IntegerField(primary_key=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    company = models.DecimalField(max_digits=5, decimal_places=2)
    prize = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s the bus no for mechanical update:" % self.registerNo

class Electrical(models.Model):
    registerNo = models.IntegerField(primary_key=True)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    company = models.DecimalField(max_digits=5, decimal_places=2)
    prize = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s the bus no for electrical update:" % self.registerNo

class spareExpenses(models.Model):
  registerNo = models.IntegerField(primary_key=True)
  mechanical = models.OneToOneField(
        Mechanical,
        on_delete=models.CASCADE
    )
  electrical = models.OneToOneField(
        Electrical,
        on_delete=models.CASCADE
    )
  glassPrice = models.DecimalField(max_digits=5, decimal_places=2)
  FRP_Price = models.DecimalField(max_digits=5, decimal_places=2)
  tinkering = models.DecimalField(max_digits=5, decimal_places=2)
  oilAndLubricant = models.DecimalField(max_digits=5, decimal_places=2)
  blackSmith = models.DecimalField(max_digits=5, decimal_places=2)
  stickering = models.CharField(max_length=100)
  # photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  # photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  date_updated = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return "%s the bus no is:" % self.registerNo

