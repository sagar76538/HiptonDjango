from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Sagar Arora</h1>")

def get_product(request, id):
    return HttpResponse(f"<h1> Product id: {id}</h1>")
    
