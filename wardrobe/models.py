from django.db import models

# Create your models here.
class ClothingItem(models.Model):
    """Model representing an individual item of clothing."""
    
    # REQUIRED FIELDS
    name = models.CharField(max_length=50, unique=True)
    
    # OPTIONAL FIELDS
    picture = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    # Stores numbers with two decimal places up to one billion.
    purchase_date = models.DateField(null=True, blank=True)
    # If not provided, use the earliest wear date.
    previous_wears = models.IntegerField(null=True, blank=True)
    # If provided, add to the number of wear dates.
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """Returns a string for representing a ClothingItem object."""
        return self.name
        
    def get_absolute_url(self):
        pass
        
class WearDate(models.Model):
    """Model representing a date on which a clothing item was worn."""
    
    # REQUIRED FIELDS
    date = models.DateField(unique=True)
    clothing_items = models.ManyToManyField(ClothingItem)
    # Belongs to WearDate because clothes will be added to dates on a calendar 
    # form.
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        """Returns a string for representing a WearDate object."""
        return self.date.isoformat()
        
    def get_absolute_url(self):
        pass
        