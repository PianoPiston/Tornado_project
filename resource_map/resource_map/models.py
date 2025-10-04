from django.db import models

# Choices for resource types to ensure data consistency.
PROFESSIONAL_RESOURCE_CHOICES = [
    ('doctor', 'Doctor'),
    ('nurse', 'Nurse'),
    ('engineer', 'Engineer'),
    ('electrician', 'Electrician'),
    ('mechanic', 'Mechanic'),
]

CIVILIAN_RESOURCE_CHOICES = [
    ('car', 'Car'),
    ('tractor', 'Tractor'),
    ('generator', 'Generator'),
    ('food_supply', 'Food Supply'),
    ('shelter', 'Shelter'),
    ('tools', 'Tools'),
]

class ProfessionalResource(models.Model):
    """
    Represents professional expertise or services available at a specific location.
    """
    name = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50, choices=PROFESSIONAL_RESOURCE_CHOICES)
    specialty = models.CharField(max_length=100, help_text="e.g., Cardiologist, Diesel engines")
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_resource_type_display()}: {self.name} ({self.specialty})"

class CivilianResource(models.Model):
    """
    Represents a physical resource volunteered by a civilian.
    """
    contact_person = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50, choices=CIVILIAN_RESOURCE_CHOICES)
    description = models.TextField(help_text="e.g., 4-door sedan, 5kW petrol generator")
    quantity = models.CharField(max_length=50, default="1")
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_resource_type_display()} from {self.contact_person}"
