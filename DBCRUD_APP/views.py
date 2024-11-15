from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Vehicles
# Create your views here.
def add_vehicle(request):
    #check for the method with an if statement
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Vehicles.objects.create(name=name, description=description)
        return redirect('item_list')
    #this is used if you are reusing the html template.
    #use reverse for urls for code maintainability
    context = {
        'action_url':reverse('create_item'),
        'name':'',
        'description':'',
    }
    return render(request, 'form.html', context)
def list_vehicles(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'item_list.html',{'vehicles':vehicles})
def delete(request, id):
    vehicle = Vehicles.objects.get(id=id)
    # vehicle= get_object_or_404(Vehicles, id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('item_list')
    return  render(request, 'confirm_delete.html',{'vehicle':vehicle})
def update(request, id):
    vehicle = Vehicles.objects.get(id=id)
    if request.method == 'POST':
        vehicle.name = request.POST.get('name')
        vehicle.description = request.POST.get('description')
        vehicle.save()
        return redirect('item_list')
    context={
        'action_url':reverse('update_item', kwargs={'id':id}),
        'name':vehicle.name,
        'description':vehicle.description,
    }
    return render(request, 'form.html',context)