import csv
from django.core.management.base import BaseCommand
from catalog.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                phone, created = Phone.objects.update_or_create(
                    id=int(row['id']),
                    defaults={
                        'name': row['name'],
                        'price': float(row['price']),
                        'image': row['image'],
                        'release_date': row['release_date'],
                        'lte_exists': row['lte_exists'].lower() == 'true',
                    }
                )
                self.stdout.write(f'{"Created" if created else "Updated"}: {phone.name}')
        self.stdout.write(self.style.SUCCESS('Import completed'))
