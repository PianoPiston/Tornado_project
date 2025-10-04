import random
from django.core.management.base import BaseCommand
from resource_map.models import ProfessionalResource, CivilianResource

#import os
#import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resourcemap.settings")
# django.setup()

# Bounding box for Finland
FINLAND_COORDS = {
    'lat_min': 60.0,
    'lat_max': 70.0,
    'lon_min': 20.0,
    'lon_max': 31.5,
}

PROFESSIONAL_SAMPLES = [
    {'type': 'doctor', 'name': 'Dr. Aalto', 'specialty': 'General Surgery'},
    {'type': 'doctor', 'name': 'Dr. Virtanen', 'specialty': 'Pediatrics'},
    {'type': 'nurse', 'name': 'Nurse Korhonen', 'specialty': 'Emergency Care'},
    {'type': 'engineer', 'name': 'Eng. Nieminen', 'specialty': 'Civil Engineering'},
    {'type': 'electrician', 'name': 'Elec. Laine', 'specialty': 'High Voltage Systems'},
    {'type': 'mechanic', 'name': 'Mech. Heikkinen', 'specialty': 'Heavy Machinery'},
]

CIVILIAN_SAMPLES = [
    {'type': 'car', 'contact': 'Matti', 'desc': 'Volvo V70', 'qty': '1 vehicle'},
    {'type': 'tractor', 'contact': 'Liisa', 'desc': 'Valtra T-Series', 'qty': '1 tractor'},
    {'type': 'generator', 'contact': 'Pekka', 'desc': 'Honda 5kW Petrol', 'qty': '1 unit'},
    {'type': 'food_supply', 'contact': 'Anna', 'desc': 'Canned goods', 'qty': '50 kg'},
    {'type': 'shelter', 'contact': 'Eemeli', 'desc': 'Basement shelter', 'qty': '5 person capacity'},
    {'type': 'tools', 'contact': 'Sofia', 'desc': 'General mechanics toolkit', 'qty': '1 set'},
]


class Command(BaseCommand):
    help = 'Populates the database with sample resource data within Finland.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data...')
        ProfessionalResource.objects.all().delete()
        CivilianResource.objects.all().delete()

        self.stdout.write('Creating new sample data...')

        # Create 15 professional resources
        for _ in range(15):
            sample = random.choice(PROFESSIONAL_SAMPLES)
            ProfessionalResource.objects.create(
                name=sample['name'],
                resource_type=sample['type'],
                specialty=sample['specialty'],
                latitude=random.uniform(FINLAND_COORDS['lat_min'], FINLAND_COORDS['lat_max']),
                longitude=random.uniform(FINLAND_COORDS['lon_min'], FINLAND_COORDS['lon_max']),
            )

        # Create 15 civilian resources
        for _ in range(15):
            sample = random.choice(CIVILIAN_SAMPLES)
            CivilianResource.objects.create(
                contact_person=sample['contact'],
                resource_type=sample['type'],
                description=sample['desc'],
                quantity=sample['qty'],
                latitude=random.uniform(FINLAND_COORDS['lat_min'], FINLAND_COORDS['lat_max']),
                longitude=random.uniform(FINLAND_COORDS['lon_min'], FINLAND_COORDS['lon_max']),
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample data.'))
