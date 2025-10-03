from django import forms
from .models import CivilianResource

class CivilianResourceForm(forms.ModelForm):
    """
    A form for civilians to submit their resources.
    The location fields are hidden and will be populated by JavaScript on the frontend.
    """
    class Meta:
        model = CivilianResource
        fields = ['contact_person', 'resource_type', 'description', 'quantity', 'latitude', 'longitude']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contact_person'].widget.attrs.update({'placeholder': 'Your Name or Contact Info'})
        self.fields['description'].widget.attrs.update({'placeholder': 'e.g., Toyota Hilux, 4 people capacity'})
        self.fields['quantity'].widget.attrs.update({'placeholder': 'e.g., 1 vehicle, 10kg of potatoes'})
