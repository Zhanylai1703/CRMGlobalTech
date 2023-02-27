from django import forms
from .models import Customer, Employee, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'age', 'gender', 'location')


    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'age', 'gender', 'location')



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('product', 'employee', 'customer', 'date')
        