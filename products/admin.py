from django.contrib import admin
from .models import Product, Stock, Supplier
# Register your models here.

# Necesario para poder ver los campos ocultos 'created' y 'updated'
class SupplierAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Filtro personalizado para filtrar por proveedor
class SupplierFilter(admin.SimpleListFilter):
    title = 'Proveedor'
    parameter_name = 'supplier'

    def lookups(self, request, model_admin):
        suppliers = Supplier.objects.all()
        return [(supplier.id, supplier.name) for supplier in suppliers]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(product__supplier_id=self.value())
        return queryset

class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'quantity', 'get_supplier')
    list_filter = (SupplierFilter, 'product')

    def get_supplier(self, obj):
        return obj.product.supplier.name  # Ahora usa 'supplier' en minúsculas
    get_supplier.short_description = 'Proveedor'



admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Stock, StockAdmin)

