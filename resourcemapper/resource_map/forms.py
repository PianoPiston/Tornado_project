from django import forms
from .models import CivilianResource, ProfessionalResource

class CivilianResourceForm(forms.ModelForm):
    """
    A form for civilians to submit their resources.
    The location fields are hidden and will be populated by JavaScript on the frontend.
    """
    class Meta:
        model = CivilianResource
        fields = ['alias', 'contact_person', 'resource_type', 'description', 'quantity', 'latitude', 'longitude']
        widgets = {
            'alias': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 3}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contact_person'].widget.attrs.update({'placeholder': 'Contact Info'})
        self.fields['description'].widget.attrs.update({'placeholder': 'e.g., Toyota Hilux, 4 people capacity'})
        self.fields['quantity'].widget.attrs.update({'placeholder': 'e.g., 1 vehicle, 10kg of potatoes'})


class ProfessionalResourceForm(forms.ModelForm):
    """
    A form for professionals to submit their expertise or service.
    The location fields are hidden and will be populated by JavaScript on the frontend.
    """
    class Meta:
        model = ProfessionalResource
        fields = ['alias', 'profession', 'specialty', 'latitude', 'longitude']
        widgets = {
            'specialty': forms.TextInput(),
            'alias': forms.HiddenInput(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['specialty'].widget.attrs.update({'placeholder': 'e.g., Cardiologist, Diesel mechanic, Web developer'})