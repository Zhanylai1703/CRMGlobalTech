from django.db import models
from apps.markets.models import Location, Product
from django.urls import reverse_lazy
from django.shortcuts import redirect


class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('customer_detail', args=[str(self.id)])



class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse_lazy('employee-detail', args=[str(self.id)])




class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.product} - {self.date}"
    

    def get_absolute_url(self):
        return reverse_lazy('order-detail', args=[str(self.id)])
    



