from rest_framework import viewsets
from .models import Product, Stock, Supplier
from .serializers import ProductSerializer, StockSerializer, SupplierSerializer
from .filters import ProductFilter
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


# Vista de productos + filtro por proveedores ProductFilter
class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]  # Indicamos que vamos a usar filtrado
    filterset_class = ProductFilter  # Apuntamos a la clase de filtros que hemos definido



# Defino el filtro para las búsquedas generales de la tabla productos (code, name, supplier, description)
class ProductoSearchFilter(filters.FilterSet):
    search = filters.CharFilter(method='search_filter', label="Buscar")

    class Meta:
        model = Product
        fields = []  # Dejamos vacío porque manejaremos todo en el método personalizado

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(code__icontains=value) |
            Q(name__icontains=value) |
            Q(supplier__name__icontains=value) | 
            Q(description__icontains=value)
        )

# Vista de productos + filtro search pro varios campos 
class ProductoSearchView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductoSearchFilter  
    # Filtro para buscar por varios campos




# Vista del stock
class StockViewset(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

# Vista de los proveedores
class SupplierViewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class =  SupplierSerializer


