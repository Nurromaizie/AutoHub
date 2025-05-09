from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50, default='Unknown')  
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    seats = models.IntegerField()
    body_type = models.CharField(max_length=50)
    image_url = models.URLField()

    def __str__(self):
        return f"{self.brand} {self.name}"
