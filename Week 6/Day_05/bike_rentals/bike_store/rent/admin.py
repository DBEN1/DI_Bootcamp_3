from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Address, Customer, RentalStation, Vehicle, VehicleType, VehicleSize

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(RentalStation)
admin.site.register(Vehicle)
admin.site.register(VehicleType)
admin.site.register(VehicleSize)
