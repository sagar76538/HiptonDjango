from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
category_choices = (
                    ("FAN", "FAN",), 
                    ("LED", "LED"), 
                    ("FAN REGULATOR", "FAN REGULATOR"), 
                    ("SWITCH","SWITCH"),  
                    ("OTHER", "OTHER")
                    )

class Categories(models.Model):
    __tablename__ = "Categories"
    category = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.category
    
    @staticmethod
    def get_all():
        return Categories.objects.all()
    
    @staticmethod
    def get_category(id):
        return Categories.objects.get(id=id)
    
    class Meta:
        ordering = ["id"]
    

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products')
    description = models.JSONField(null = True, default={"param1": "value1", 
                                                         "param2": "value2", 
                                                         "param3": "value3", 
                                                         "param4": "value4", 
                                                         "param5": "value5", 
                                                         "param6": "value6", 
                                                         "param7": "value7", 
                                                         "param8": "value8"})
    
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" style="width: 45px; height:45px; border-radius: 50%;" />')
        else:
            return 'No Image Found'
        
    image_tag.short_description = 'Image'
    

    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all():
        return Product.objects.all()
    
    @staticmethod
    def get_product(id):
        return Product.objects.get(id=id)
    
    @staticmethod
    def get_product_by_category(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()
    
    class Meta:
        ordering = ['-id']