import random
from django.core.management.base import BaseCommand
from resource_map.models import ProfessionalResource, CivilianResource

#import os
#import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resourcemap.settings")
# django.setup()

# Bounding box for Finland
FINLAND_COORDS = {
    'lat_min': 62.0,
    'lat_max': 68.0,
    'lon_min': 23.0,
    'lon_max': 30.5,
}

PROFESSIONAL_SAMPLES = [
    {'type': 'doctor', 'alias': 'Dave','name': 'Dave', 'specialty': 'General Surgery'},
    {'type': 'doctor', 'alias': 'Jorma','name': 'Jorma', 'specialty': 'Pediatrics'},
    {'type': 'nurse', 'alias': 'John','name': 'John', 'specialty': 'Emergency Care'},
    {'type': 'engineer', 'alias': 'Taavi','name': 'Taavi', 'specialty': 'Civil Engineering'},
    {'type': 'electrician', 'alias': 'Peter','name': 'Peter', 'specialty': 'High Voltage Systems'},
    {'type': 'mechanic', 'alias': 'Petri','name': 'Petri', 'specialty': 'Heavy Machinery'},
]

CIVILIAN_SAMPLES = [
    {'type': 'car', 'contact': 'matti.meikäläinen@gmail.com', 'desc': 'Volvo V70', 'qty': '1 vehicle'},
    {'type': 'tractor', 'contact': '0231223042', 'desc': 'Valtra T-Series', 'qty': '1 tractor'},
    {'type': 'generator', 'contact': 'pekka.pouta@hotmail.com', 'desc': 'Honda 5kW Petrol', 'qty': '1 unit'},
    {'type': 'food supply', 'contact': 'paavo.pesusieni@bikinibottom.org', 'desc': 'Canned goods', 'qty': '50 kg'},
    {'type': 'shelter', 'contact': '0442315829', 'desc': 'Basement shelter', 'qty': '5 person capacity'},
    {'type': 'tools', 'contact': 'pekka.pouta@hotmail.com', 'desc': 'General mechanics toolkit', 'qty': '1 set'},
]


class Command(BaseCommand):
    help = 'Populates the database with sample resource data within Finland.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        ProfessionalResource.objects.all().delete()
        CivilianResource.objects.all().delete()

        self.stdout.write('Creating new sample data...')

        # Create 15 professional resources
        for sample in PROFESSIONAL_SAMPLES:
            ProfessionalResource.objects.create(
                alias=sample['alias'],
                profession=sample['type'],
                specialty=sample['specialty'],
                latitude=random.uniform(FINLAND_COORDS['lat_min'], FINLAND_COORDS['lat_max']),
                longitude=random.uniform(FINLAND_COORDS['lon_min'], FINLAND_COORDS['lon_max']),
            )

        # Create 15 civilian resources
        for sample in CIVILIAN_SAMPLES:
            CivilianResource.objects.create(
                contact_person=sample['contact'],
                resource_type=sample['type'],
                description=sample['desc'],
                quantity=sample['qty'],
                latitude=random.uniform(FINLAND_COORDS['lat_min'], FINLAND_COORDS['lat_max']),
                longitude=random.uniform(FINLAND_COORDS['lon_min'], FINLAND_COORDS['lon_max']),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))
