from django.db import models

# Create your models here.
class ClothingTag(models.Model):
    """Model representing a user-defined tag to be applied to clothing items.
    Tags are grouped into categories such as colors, brands, clothing types,
    etc."""
    
    BRAND = 'BR'
    COLOR = 'CO'
    TYPE = 'TY'
    OTHER = 'OT'
    
    TAG_CATEGORY_CHOICES = [
        (BRAND, 'Brand'),
        (COLOR, 'Color'),
        (TYPE, 'Type'),
        (OTHER, 'Other'),
    ]
    
    # REQUIRED FIELDS
    name = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200, choices=TAG_CATEGORY_CHOICES)
    
    class Meta:
        ordering = ['category', 'name']
        
    def __str__(self):
        """Returns a string for representing a ClothingTag object."""
        return self.name
        
    def get_absolute_url(self):
        pass

class ClothingItem(models.Model):
    """Model representing an individual item of clothing."""
    
    # REQUIRED FIELDS
    name = models.CharField(max_length=200, unique=True)
    
    # OPTIONAL FIELDS
    picture = models.ImageField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, null=True, blank=True)
    # Stores numbers with two decimal places up to one billion (allows negatives).
    purchase_date = models.DateField(null=True, blank=True)
    # If not provided, use the earliest wear date.
    previous_wears = models.PositiveIntegerField(null=True, blank=True)
    # If provided, add to the number of wear dates.
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(ClothingTag)
    # Belongs to ClothingItem because tags will be added to clothes in the
    # form, not the other way around.
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        """Returns a string for representing a ClothingItem object."""
        return self.name
        
    def get_absolute_url(self):
        pass
        
class ClothingWearDate(models.Model):
    """Model representing a date on which a clothing item was worn."""
    
    # REQUIRED FIELDS
    date = models.DateField(unique=True)
    clothing_items = models.ManyToManyField(ClothingItem)
    # Belongs to WearDate because clothes will be added to dates on a calendar 
    # form.
    
    class Meta:
        ordering = ['date']
    
    def __str__(self):
        """Returns a string for representing a ClothingWearDate object."""
        return self.date.isoformat()
        
    def get_absolute_url(self):
        pass
        