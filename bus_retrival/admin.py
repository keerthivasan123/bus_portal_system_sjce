from django.contrib import admin

# Register your models here.
from .models import Mechanical,Electrical,spareExpenses,weeklyExpenses,tyres,dieselFilling

admin.site.register(spareExpenses)
admin.site.register(Mechanical)
admin.site.register(Electrical)
admin.site.register(weeklyExpenses)
admin.site.register(tyres)
admin.site.register(dieselFilling)
