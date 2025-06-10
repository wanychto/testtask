import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
from trucks.models import Truck

def point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False
    
    for px, py in polygon:
        if x == px and y == py:
            return True
    
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        
        if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                return True

        if ((y1 > y) != (y2 > y)):
            x_intersect = (y - y1) * (x2 - x1) / (y2 - y1) + x1
            if x <= x_intersect:
                inside = not inside
    
    return inside
