from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.core.serializers import serialize
from django.views.decorators.http import require_POST
from .models import ProfessionalResource, CivilianResource
from .forms import CivilianResourceForm, ProfessionalResourceForm
from django.db.models import Q

@require_POST
def update_status(request, resource_type, resource_id):
    """
    Allows a user to update the status of a resource.
    Professionals -> set status='deceased'
    Civilians -> set status='destroyed'
    """
    if resource_type == "professional":
        resource = get_object_or_404(ProfessionalResource, id=resource_id)
        new_status = "inactive"
    elif resource_type == "civilian":
        resource = get_object_or_404(CivilianResource, id=resource_id)
        new_status = "destroyed"
    else:
        messages.error(request, "Invalid resource type.")
        return redirect("/dashboard")

    resource.status = new_status
    resource.save()

    messages.success(request, f"{resource} marked as {new_status}.")
    return redirect("/dashboard")

def map_view(request):
    """
    Main view to display the map and resource tables.
    Fetches all resources and passes them to the template as JSON.
    """
    searchterm = request.GET.get('searchterm', '').strip()

    if not searchterm:
        professional_resources = ProfessionalResource.objects.all()
        civilian_resources = CivilianResource.objects.all()
    else:
        prof_query = Q()
        civ_query = Q()
        prof_query |= Q(profession__icontains=searchterm)
        prof_query |= Q(specialty__icontains=searchterm)
        prof_query |= Q(alias__icontains=searchterm)

        civ_query |= Q(contact_person__icontains=searchterm)
        civ_query |= Q(resource_type__icontains=searchterm)
        civ_query |= Q(description__icontains=searchterm)
        civ_query |= Q(alias__icontains=searchterm)

        professional_resources = ProfessionalResource.objects.filter(prof_query).distinct()
        civilian_resources = CivilianResource.objects.filter(civ_query).distinct()


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

def welcome_view(request):
    return render(request, 'resource_map/welcome.html')

def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            request.session['username'] = name  # store in session
            return redirect('/dashboard/')
    return render(request, 'resource_map/login.html')

def dashboard_view(request):
    name = request.session.get('username')
    if not name: 
        return redirect("/login")
    professional_resources = ProfessionalResource.objects.filter(alias=name)
    civilian_resources = CivilianResource.objects.filter(alias=name)

    # Serialize querysets to JSON to be safely used in JavaScript
    professional_resources_json = serialize('json', professional_resources)
    civilian_resources_json = serialize('json', civilian_resources)

    context = {
        'name': name,
        'professional_resources': professional_resources,
        'civilian_resources': civilian_resources,
        'professional_resources_json': professional_resources_json,
        'civilian_resources_json': civilian_resources_json,
    }
    return render(request, 'resource_map/dashboard.html', context)

def logout(request):
    request.session.flush()
    return redirect("/")

def add_resource_view(request):
    """
    Single page where user chooses to add either a professional skill or civilian resource.
    """
    name = request.session.get("username")
    if not name:
        return redirect('/login')

    resource_type = request.GET.get('type')  # 'civilian' or 'professional'

    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'professional':
            post_data = request.POST.copy()
            post_data["alias"] = name
            form = ProfessionalResourceForm(post_data)
            if form.is_valid():
                form.save()
                return redirect('/dashboard')
        elif form_type == 'civilian':
            post_data = request.POST.copy()
            post_data["alias"] = name
            form = CivilianResourceForm(post_data)
            if form.is_valid():
                form["alias"] == request.session.get("username")
                form.save()
                return redirect('/dashboard')
        else:
            form = None
    else:
        # When user selects from dropdown (?type=civilian or ?type=professional)
        if resource_type == 'professional':
            form = ProfessionalResourceForm()
        elif resource_type == 'civilian':
            form = CivilianResourceForm()
        else:
            form = None  # No form until selection

    return render(request, 'resource_map/add_resource.html', {
        'form': form,
        'resource_type': resource_type,
    })