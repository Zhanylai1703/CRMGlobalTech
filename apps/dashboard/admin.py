from django.contrib import admin
from .models import Customer, Employee, Order

# Register your models here.

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Order)