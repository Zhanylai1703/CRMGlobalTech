from django.core.management.base import BaseCommand
import csv
from ...models import Product


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='path to csv file')

    def handle(self, *args, **kwargs):
        path = kwargs.get('path')
        file = open(path)
        csvreader = csv.reader(file)
        products = []
        for row in csvreader:
            products.append(Product(name=row[0], description=row[1], price=row[-1]))
        Product.objects.bulk_create(products)