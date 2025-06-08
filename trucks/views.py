from django.shortcuts import render
from .models import Truck

def truck_list(request):
    trucks = Truck.objects.all()
    return render(request, 'trucks/truck_list.html', {'trucks': trucks}) 
