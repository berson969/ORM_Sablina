import csv

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
           date = datetime.strptime( phone['release_date'], '%Y-%m-%d')
           Phone.odjects.create( name=phone['name'],
                                 image=phone['image'],
                                 price=phone['price'],
                                 release_date=date,
                                 lte_exists=bool(phone['lte_exist']),
                                 slug=slugify(phone['name']))
           print('Все модели созданы в базе данных')
