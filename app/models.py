from django.db import models

# Create your models here.
category_choices = (
                    ("FAN", "FAN",), 
                    ("LED", "LED"), 
                    ("FAN REGULATOR", "FAN REGULATOR"), 
                    ("SWITCH","SWITCH"),  
                    ("OTHER", "OTHER")
                    )

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=category_choices, null=True)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=None)
    description = models.JSONField(null = True, default={"power": "220V"})

    def __str__(self):
        return self.name
