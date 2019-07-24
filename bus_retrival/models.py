from django.db import models
from datetime import datetime  
class Mechanical(models.Model):
    registerNo = models.IntegerField(primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.DecimalField(max_digits=10, decimal_places=2)
    prize = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "%s the bus no for mechanical update:" % self.registerNo

class Electrical(models.Model):
    registerNo = models.IntegerField(primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.DecimalField(max_digits=10, decimal_places=2)
    prize = models.DecimalField(max_digits=10, decimal_places=2)

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
  glassPrice = models.DecimalField(max_digits=10,decimal_places=2)
  FRP_Price = models.DecimalField(max_digits=10,decimal_places=2)
  tinkering = models.DecimalField(max_digits=10,decimal_places=2)
  oilAndLubricant = models.DecimalField(max_digits=10,decimal_places=2)
  blackSmith = models.DecimalField(max_digits=10,decimal_places=2)
  stickering = models.CharField(max_length=100)
  date_updated = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return "Spare brought for %s" % self.registerNo

class dieselFilling(models.Model):
  quantity = models.DecimalField(max_digits=10, decimal_places=2)
  dateOfFilling = models.DateTimeField(default=datetime.now, blank=True)
  startKm = models.IntegerField()
  def __str__(self):
    return "Filled on %s" % self.dateOfFilling
class tyres(models.Model):
  dateOfChanging = models.DateTimeField(default=datetime.now, blank=True)
  KmChanged = models.IntegerField()
  def __str__(self):
    return "Tyre changed on %s" % self.dateOfChanging

class weeklyExpenses(models.Model):
  registerNo = models.IntegerField(primary_key=True)
  parkingLocation = models.CharField(max_length=100)
  parkingCharges = models.DecimalField(max_digits=10,decimal_places=2)
  dieselFilling = models.OneToOneField(
        dieselFilling,
        on_delete=models.CASCADE
    )
  tyres = models.OneToOneField(
        tyres,
        on_delete=models.CASCADE
    )
  def __str__(self):
    return "Weekly expenses for %s" % self.registerNo



