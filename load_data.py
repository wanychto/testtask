from trucks.models import Truck

trucks_data= [
    {
        'board_number' : '102',
        'model' : 'belaz',
        'max_capacity' : 120, 
        'load_weight' : 125, 
        'silicon_dioxide_percent' : 30,
        'iron_percent' : 65
    },
    {
        'board_number' : 'K103',
        'model' : 'Komatsu',
        'max_capacity' : 110, 
        'load_weight' : 120, 
        'silicon_dioxide_percent' : 35,
        'iron_percent' : 62
    }
]
for data in trucks_data:
    Truck.objects.create(**data)