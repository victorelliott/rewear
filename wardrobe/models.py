from django.db import models

# Create your models here.
class Garment(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
        
class Date(models.Model):
    date_worn = models.DateField()
    garments = models.ManyToManyField(Garment)
    def __str__(self):
        return self.date_worn.isoformat()