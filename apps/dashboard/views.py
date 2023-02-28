from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Customer, Order, Employee
from apps.markets.models import Product
from django.db.models import Sum
from django.shortcuts import render


def index(request):
    return render(request,'base.html')


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer/list.html'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer/customer_detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.object
        orders = Order.objects.filter(customer=customer)
        total = orders.aggregate(Sum('product__price'))
        context['orders'] = orders
        context['total'] = total['product__price__sum']
        return context
    



class CustomerCreateView(CreateView):
    template_name = 'customer/customer_create.html'
    model = Customer
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('customer-list')

class CustomerUpdateView(UpdateView):
    template_name = 'customer/customer_update.html'
    model = Customer
    fields = ['name', 'age', 'gender', 'location']

class CustomerDeleteView(DeleteView):
    template_name = 'customer/customer_delete.html'
    model = Customer
    success_url = reverse_lazy('customer-list')



# CRUD for Employee

class EmployeeListView(ListView):
    model = Employee
    template_name = 'Employee/employee_list.html'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'Employee/employee_detail.html'
    slug_field = 'id'
    slug_url_kwarg = 'id'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employee = self.object
        orders = Order.objects.filter(employee=employee)
        total = orders.aggregate(Sum('product__price'))
        context['orders'] = orders
        context['total'] = total['product__price__sum']
        return context


class EmployeeCreateView(CreateView):
    template_name = 'Employee/employee_create.html'
    model = Employee
    fields = ['name', 'age', 'gender', 'location']
    success_url = reverse_lazy('employee_list')


class EmployeeUpdateView(UpdateView):
    template_name = 'Emploee/employee_update.html'
    model = Employee
    fields = ['name', 'age', 'gender', 'location']

class EmployeeDeleteView(DeleteView):
    template_name = 'Employee/employee_delete.html'
    model = Employee
    success_url = reverse_lazy('employee_list')



# CRUD for Order


class OrderListView(ListView):
    model = Order
    template_name = 'Order/orderlist.html'

class OrderCreateView(CreateView):
    template_name = 'Order/ordercreate.html'
    model = Order
    fields = ['product', 'employee', 'customer', 'date']
    success_url = reverse_lazy('order_list')

class OrderDetailView(DetailView):
    template_name = 'Order/orderdetail.html'
    model = Order

class OrderUpdateView(UpdateView):
    template_name = 'Order/orderupdate.html'
    model = Order
    fields =  ['product', 'employee', 'customer', 'date']
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'Order/orderdelete.html'
    success_url = reverse_lazy('order_list')