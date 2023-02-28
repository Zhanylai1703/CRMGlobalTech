from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from decimal import Decimal
from apps.dashboard.models import Customer, Order, Employee
from apps.markets.models import Product
from .views import CustomerDetailView

class CustomerDetailViewTestCase(TestCase):
    
    def setUp(self):
        self.customer = Customer.objects.create(name='Nikita', age=17)
        self.product = Product.objects.create(name='Website', price='500.00')
        self.order = Order.objects.create(customer=self.customer, product=self.product)
    
    def test_get_context_data(self):
        url = reverse('customer_detail', kwargs={'pk': self.customer.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'customer_detail.html')
        self.assertEqual(response.context['customer'], self.customer)
        self.assertEqual(list(response.context['orders']), [self.order])
        self.assertEqual(response.context['total'], Decimal('10.00'))
    
    def tearDown(self):
        self.order.delete()
        self.product.delete()
        self.customer.delete()



