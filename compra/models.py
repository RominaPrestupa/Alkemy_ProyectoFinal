from django.db import models

class Proveedor(models.Model):
    razon_social = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    dni = models.IntegerField(blank = False)

    class Meta:
        ordering = ('razon_social',) 
    
    def __str__(self):
        return self.razon_social
    
   
class Producto(models.Model):
    nombre_producto = models.CharField(max_length = 200, unique = True)
    precio = models.DecimalField(max_digits = 10, decimal_places = 1, blank = False)
    stock_actual = models.IntegerField(blank = False)
    proveedor = models.ForeignKey(Proveedor, on_delete = models.PROTECT, related_name = 'productos', blank = False)

    def __str__(self):
        return self.nombre_producto