from django.db import models

# Create your models here.

# Modelo proveedor
class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name= 'Nombre')
    contact_data = models.TextField(verbose_name='Datos Contacto')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Pasos para convertir en español la aplación en el admin 
    
    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'
        db_table = "suppliers"
        ordering = ['name']


    # Con esta función logro mostrar en la lista de proyectos del admin, todos los proyectos con su titulo
    def __str__(self):
        return self.name

# Modelo Articulo
class Product(models.Model):

    color_choices = [
        ('Negro', 'Negroooooooo'),
        ('Blanco', 'Blanco'),
        ('Suela', 'Suelaaaaaaaaaaa'),
        ('camel', 'Camel'),
        ('Plata', 'Plata'),
    ]

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Proveedor")
    code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Codigo")
    name = models.CharField(max_length=255, verbose_name="Nombre")
    image = models.ImageField(upload_to='products', default='imagen_default.png', verbose_name='Foto del calzado')
    description = models.TextField(blank=True, null=True, verbose_name="Descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    color = models.CharField(max_length=20, choices= color_choices,default='Negro', blank=True, null=True, verbose_name="Color")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'articulo'
        verbose_name_plural = 'articulos'
        db_table = "products"
        ordering = ['name']


    # Con esta función logro mostrar en la lista de proyectos del admin, todos los proyectos con su titulo
    def __str__(self):
        return self.name
    

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Artículo")
    size = models.PositiveIntegerField(verbose_name="Talle")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Cantidad en stock")

    class Meta:
        unique_together = ('product', 'size')
        verbose_name = "Inventario"
        verbose_name_plural = "Inventarios"

    def __str__(self):
        return f'{self.product.name} - Talle {self.size}: {self.quantity} en stock'