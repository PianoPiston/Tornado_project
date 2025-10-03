from django.shortcuts import render, redirect
from django.core.serializers import serialize
import json
from .models import ProfessionalResource, CivilianResource
from .forms import CivilianResourceForm

def map_view(request):
    """
    Main view to display the map and resource tables.
    Fetches all resources and passes them to the template as JSON.
    """
    professional_resources = ProfessionalResource.objects.all()
    civilian_resources = CivilianResource.objects.all()

    # Serialize querysets to JSON to be safely used in JavaScript
    professional_resources_json = serialize('json', professional_resources)
    civilian_resources_json = serialize('json', civilian_resources)

    context = {
        'professional_resources': professional_resources,
        'civilian_resources': civilian_resources,
        'professional_resources_json': professional_resources_json,
        'civilian_resources_json': civilian_resources_json,
    }
    return render(request, 'resource_map/map.html', context)


def add_civilian_resource_view(request):
    """
    View to handle the submission of the civilian resource form.
    - On GET, it displays an empty form with a map to select a location.
    - On POST, it validates the data and saves a new CivilianResource.
    """
    if request.method == 'POST':
        form = CivilianResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map_view') # Redirect to the main map after successful submission
    else:
        form = CivilianResourceForm()

    return render(request, 'resource_map/add_resource.html', {'form': form})
