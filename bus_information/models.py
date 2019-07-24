from django.db import models
from datetime import datetime
from bus_retrival.models import spareExpenses
# Create your models here.
class basicDetail(models.Model):
  registerNo = models.IntegerField(primary_key=True)
  fcDate = models.DateTimeField(default=datetime.now, blank=True)
  permitDue = models.DecimalField(max_digits=10,decimal_places=2)
  insuranceDue = models.DecimalField(max_digits=10,decimal_places=2)
  driverName = models.CharField(max_length=100)
  seatingCapacity = models.IntegerField()
  date_updated = models.DateTimeField(default=datetime.now, blank=True)
  spareExpenses = models.ForeignKey(
        spareExpenses,
        on_delete=models.CASCADE,
        null=True
    )
  def save(self, *args, **kwargs):
        if self.spareExpenses is None:  # Set default reference
            self.spareExpenses = spareExpenses.objects.get(id=1)
        super(basicDetail, self).save(*args, **kwargs)
  def __str__(self):
    return "TN%s" % self.registerNo