from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Categories

# Create your views here.
def index(request):
    
    products = Product.get_all()
    categories = Categories.get_all()
    
    try:
        if request.method == "GET":
            category_id = request.GET.get('category_id', None)
            print('CATEGORY ID',category_id)
            if category_id:
                products = Product.get_product_by_category(category_id=category_id)
                
    except Exception as e:
        print(f"{e}")
    
    contenxt = {
        "categories": categories,
        "products": products
        }
    
    # print(contenxt)
    return render(request, 'home.html', contenxt)


def get_product(request, id):
    product = Product.get_product(id)
    context = {
        "product": product
    }
    return render(request, "product.html", context)
    
