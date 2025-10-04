from django.db import models

# Choices for resource types to ensure data consistency.
PROFESSIONAL_STATUS_CHOICES = [
    ('alive', 'Alive (Available)'),
    ('lost', 'Missing/Lost'),
    ('injured', 'Injured/Incapacitated'),
    ('deceased', 'Deceased'),
]

# Statuses for Civilian Resources (equipment/items)
CIVILIAN_STATUS_CHOICES = [
    ('active', 'Active (Available)'),
    ('destroyed', 'Destroyed/Unusable'),
    ('in_transit', 'In Transit/Unavailable'),
    ('damaged', 'Damaged/Under Repair'),
]

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

    status = models.CharField(
        max_length=20,
        choices=PROFESSIONAL_STATUS_CHOICES,
        default='alive',  # Default is 'alive'
        help_text="The current status or state of the professional resource."
    )
    
    alias = models.CharField(
        max_length=100, 
        unique=True,          # Ensures no two resources share the same public name
        null=True,            # Allows the database to store NULL (empty) for existing rows
        blank=True,           # Allows forms to submit this field empty
        help_text="A unique username to tied to your digital-ID"
    )

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

    alias = models.CharField(
        max_length=100, 
        unique=True,          # Ensures no two resources share the same public name
        null=True,            # Allows the database to store NULL (empty) for existing rows
        blank=True,           # Allows forms to submit this field empty
        help_text="A unique username to tied to your digital-ID"
    )

    status = models.CharField(
        max_length=20,
        choices=CIVILIAN_STATUS_CHOICES,
        default='active',  # Default is 'active'
        help_text="The current status or state of the civilian resource."
    )

    def __str__(self):
        return f"{self.get_resource_type_display()} from {self.contact_person}"
