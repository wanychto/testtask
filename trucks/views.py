from django.shortcuts import render, redirect
from .models import Truck, Polygon, Uploading
from .calculations import point_in_polygon
from django.contrib import messages
from django.db import transaction

def truck_list(request):
    trucks = Truck.objects.all()
    return render(request, 'trucks/truck_list.html', {'trucks': trucks}) 
DEFAULT_VALUES = {
    'polygon_coords': "30 10, 40 40, 20 40, 10 20, 30 10",
    'current_volume': 900,
    'silica_content': 34,
    'iron_content': 65
}
    
def index(request):
    trucks = Truck.objects.all()   
    polygon_obj = Polygon.objects.first()
    if not polygon_obj:
        polygon_obj = Polygon.objects.create(**DEFAULT_VALUES)

    if request.method == 'POST':
        polygon_coords = polygon_obj.polygon_coords.split(',')
        polygon_points = []
        for coord in polygon_coords:
            x, y = map(float, coord.strip().split())
            polygon_points.append((x, y))

        for truck in trucks:
            coords_key = f"coords_{truck.id}"
            coords = request.POST.get(coords_key)
            if coords:
                try:
                    x, y = map(float, coords.split())
                    truck.unloading_x = x
                    truck.unloading_y = y
                    

                    is_inside = point_in_polygon([x, y], polygon_points)
                    truck.is_unloaded_to_polygon = is_inside
                    truck.save()
                    
                    if is_inside:
                        amount = truck.load_weight
                        total_volume = polygon_obj.current_volume + amount
                        total_silica = (polygon_obj.silica_content*polygon_obj.current_volume+ amount*truck.silicon_dioxide_percent)/total_volume
                        total_iron = (polygon_obj.iron_content*polygon_obj.current_volume+ amount*truck.iron_percent)/total_volume
                        
                        polygon_obj.silica_content = total_silica 
                        polygon_obj.iron_content = total_iron 
                        polygon_obj.current_volume = total_volume
                        polygon_obj.save()
                
                except (ValueError, AttributeError) as e:
                    print(f"Ошибка обработки данных: {e}")
        return redirect('trucks:index')        
    return render(request, 'trucks/truck_list.html', {
        'trucks': trucks,
        'polygon': polygon_obj,
    })
@transaction.atomic
def reset_data(request):
    if request.method == 'POST':
        try:
            with transaction.atomic(): 
                    Polygon.objects.all().delete() 
                    new_polygon = Polygon.objects.create(**DEFAULT_VALUES)
                    print(f"Создан новый полигон: ID={new_polygon.id}")

            messages.success(request, 'Все данные успешно сброшены!')
        except Exception as e:
            transaction.set_rollback(True)
            print(f" Ошибка (транзакция откачена): {e}")
        
        return redirect('trucks:index')
    return redirect('trucks:index')
