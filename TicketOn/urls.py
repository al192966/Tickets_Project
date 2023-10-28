from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('products/<product>',views.product_cat),
]