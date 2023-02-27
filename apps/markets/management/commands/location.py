from django.core.management.base import BaseCommand
import csv
from ...models import Location


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='path to csv file')

    def handle(self, *args, **kwargs):
        path = kwargs.get('path')
        file = open(path)
        csvreader = csv.reader(file)
        locations = []
        for row in csvreader:
            locations.append(Location(country=row[0], city=row[1], district=row[-1]))
        Location.objects.bulk_create(locations)
        
        

