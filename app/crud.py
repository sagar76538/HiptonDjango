from . import models

class ProductCRUD():
    
    def get_all(self):
        obj = models.Product.objects.all().values()
        return obj
    
    def get(self, id):
        obj = models.Product.objects.filter(id=id)
        return obj