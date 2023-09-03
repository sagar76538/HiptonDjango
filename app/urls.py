from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("product/<int:id>/", views.get_product, name="product"),
]

