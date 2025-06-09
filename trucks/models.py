from django.db import models

class Truck(models.Model):
    BOARD_NUMBER_CHOICES = [
        ('101', '101'),
        ('102', '102'),
        ('K103', 'K103'),
    ]
    
    MODEL_CHOICES = [
        ('belaz', 'БЕЛАЗ'),
        ('Komatsu', 'Komatsu'),
    ]

    board_number = models.CharField(choices=BOARD_NUMBER_CHOICES, max_length=10, unique = True)
    model = models.CharField(choices=MODEL_CHOICES, max_length=10)
    max_capacity = models.IntegerField(help_text="Макс. грузоподъемность (тонн)")
    load_weight = models.IntegerField(help_text="Текущий груз(тонн)")
    silicon_dioxide_percent = models.FloatField(verbose_name="SiO₂ (%)")
    iron_percent = models.FloatField(verbose_name="Fe (%)")
    overload_percent = models.FloatField(verbose_name="Перегруз(%)", default=0.0, editable=False)

    def __str__(self):
        return f"{self.board_number} ({self.model})"
    @property
    def overload_percent(self):
        max_capacity = self.max_capacity
        return ((self.load_weight - max_capacity) / max_capacity) * 100 if self.load_weight > max_capacity else 0

class Polygon(models.Model):
    polygon_coords = models.TextField(default = "30 10,40 40,20 40,10 20,30 10")
    current_volume = models.IntegerField(help_text="Количество руды на складе", default=900)
    silica_content = models.FloatField(verbose_name="SiO₂ (%)", default=34)
    iron_content = models.FloatField(verbose_name="Fe (%)", default=65)
    def __str__(self):
        return f"Склад (объем: {self.current_volume}т)"

class Uploading(models.Model):
    truck_num = models.ForeignKey("Truck", on_delete=models.CASCADE)
    #volume = models.FloatField()
    # success = models.BooleanField(default=False)
    x_coord = models.FloatField(help_text="Координата точки разгрузки x")
    y_coord = models.FloatField(help_text="Координата точки разгрузки y")
    amount = models.IntegerField(help_text="Количество разгруженной руды")
    is_unloaded_to_polygon = models.BooleanField(default=False)
   
    def __str__(self):
        return f"Груз {self.truck.board_number} ({self.volume}т)"