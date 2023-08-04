from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


from item.models import BusinessArea, Company, Item
import csv


class Command(BaseCommand):
    help = 'writing data from static csv`s to database'

    def handle(self, *args, **options):

        file = open('static/tax.txt', 'r+')
        tax = float(file.read())
        file.close()

        for row in csv.DictReader(open('static/business_areas.csv')):
            name, create = BusinessArea.objects.get_or_create(name=row['name'])

        for row in csv.DictReader(open('static/companies.csv')):

            name, create = BusinessArea.objects.get_or_create(name=row['business_area'])

            company, create = Company.objects.get_or_create(
                company_id=row['company_id'],
                company_name=row['company_name'],
                director=row['director'],
                email=row['email'],
                business_area=BusinessArea.objects.get(name=row['business_area']),
                turnover_per_year=row['turnover_per_year'],
                tax=tax,
                is_active=True,
                created_by=User(1),
            )

        for row in csv.DictReader(open('static/items.csv')):
            name, create = BusinessArea.objects.get_or_create(name=row['business_area'])

            company, create = Item.objects.get_or_create(
                product_id=row['product_id'],
                product_name=row['product_name'],
                company=Company.objects.get(company_id=row['company_id']),
                business_area=BusinessArea.objects.get(name=row['business_area']),
                price=row['price'],
                in_market=True,
                created_by=User(1),
            )

        print ('Data Inserted into DataBase')
