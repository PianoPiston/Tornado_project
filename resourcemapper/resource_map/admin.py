from django.contrib import admin
from .models import ProfessionalResource, CivilianResource

@admin.register(ProfessionalResource)
class ProfessionalResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'specialty', 'latitude', 'longitude', 'created_at')
    list_filter = ('profession',)
    search_fields = ('name', 'specialty')

@admin.register(CivilianResource)
class CivilianResourceAdmin(admin.ModelAdmin):
    list_display = ('contact_person', 'resource_type', 'quantity', 'latitude', 'longitude', 'created_at')
    list_filter = ('resource_type',)
    search_fields = ('contact_person', 'description')