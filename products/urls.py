from django.urls import path, include
from .views import ProductViewset, StockViewset, SupplierViewset, ProductoSearchView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('supplier', SupplierViewset, basename = 'supplier')
router.register('product', ProductViewset, basename = 'product')
router.register('stock', StockViewset, basename = 'stock')

urlpatterns = router.urls

# Definimos las URL que el router manejará
urlpatterns = [
    path('', include(router.urls)),
    # proctos/search es la nueva URL de búsqueda por cualquier campo
    path('products/search/', ProductoSearchView.as_view({'get': 'list'}), name='product-search'),  
]