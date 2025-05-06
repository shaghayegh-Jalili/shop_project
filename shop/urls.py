from django.contrib import admin
from django.urls import path

from shop import views
from .views import index, store, checkout, product

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('store/', store, name='store'),
    path('checkout/', checkout, name='checkout'),
    path('product/', product, name='product'),

]
