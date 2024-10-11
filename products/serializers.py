from rest_framework import serializers
from django_filters import rest_framework as filters
from .models import Product, Stock, Supplier

class ProductSerializer(serializers.ModelSerializer):
    supplier_name = serializers.ReadOnlyField(source='supplier.name')
    # para el color lo tengo que obtener del color_choice que está en el modelo
    color_choice_description = serializers.ReadOnlyField(source='get_color_display')

    class Meta:
        model = Product
        fields = ('id', 'supplier', 'supplier_name', 'code', 'name','image', 'description','color', 'color_choice_description', 'price')

class StockSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Stock
        fields = ('id', 'product', 'size', 'quantity')

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('id', 'name', 'contact_data')

