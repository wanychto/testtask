import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
# django.setup()
from trucks.models import Truck

def point_in_polygon(point, polygon):
    """
    Проверяет, находится ли точка внутри полигона (включая границы).
    :param point: Кортеж (x, y) - проверяемая точка
    :param polygon: Список кортежей [(x1,y1), (x2,y2), ...] - вершины полигона
    :return: True если точка внутри или на границе, иначе False
    """
    x, y = point
    n = len(polygon)
    inside = False
    
    # Сначала проверяем, является ли точка вершиной полигона
    for px, py in polygon:
        if x == px and y == py:
            return True
    
    # Проверяем все стороны полигона
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        
        # Проверка, лежит ли точка на текущем отрезке
        # Уравнение прямой: (x - x1)/(x2 - x1) = (y - y1)/(y2 - y1)
        # Или (x - x1)*(y2 - y1) = (y - y1)*(x2 - x1)
        if (x - x1) * (y2 - y1) == (y - y1) * (x2 - x1):
            # Проверяем, что точка находится между вершинами отрезка
            if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
                return True
        
        # Алгоритм трассировки луча
        if ((y1 > y) != (y2 > y)):
            x_intersect = (y - y1) * (x2 - x1) / (y2 - y1) + x1
            if x <= x_intersect:
                inside = not inside
    
    return inside

# print(point_in_polygon(([30, 30]), ([(30,10), (40, 40), (20,40), (10, 30)])))