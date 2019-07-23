from django.contrib import admin

# Register your models here.
from .models import Mechanical,Electrical,spareExpenses

admin.site.register(spareExpenses)
admin.site.register(Mechanical)
admin.site.register(Electrical)