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

    def __str__(self):
        return f"{self.board_number} ({self.model})"
