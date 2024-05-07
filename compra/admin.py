from django.contrib import admin
from compra.models import Producto, Proveedor

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre_producto','id', 'precio', 'stock_actual']
    search_fields = ['nombre_producto', 'id']
    list_filter = ['proveedor']
    autocomplete_fields = ['proveedor']


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ['razon_social', 'nombre','apellido', 'dni']
    search_fields = ['dni', 'razon_social']
