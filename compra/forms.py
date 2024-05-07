from django import forms
from django.core.exceptions import ValidationError
from compra.models import Producto, Proveedor


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio', 'stock_actual', 'proveedor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_producto'].widget.attrs.update({'class': 'form-control'})
        self.fields['precio'].widget.attrs.update({'class': 'form-control'})
        self.fields['stock_actual'].widget.attrs.update({'class':'form-control'})
        self.fields['proveedor'].widget.attrs.update({'class':'form-control'})
        
    
    def clean_nombre_producto(self):
        nombre = self.cleaned_data.get('nombre_producto')
        if not nombre:
            raise ValidationError('Campo obligatorio')
        return nombre

    def clean_precio_producto(self):
        precio = self.cleaned_data.get('precio')
        if not precio:
            raise ValidationError("Campo obligatorio")     
        return precio
    

    def clean_stock_producto(self):
        stock = self.cleaned_data.get('stock_actual')
        print('valor stock recibido', stock)
        if not stock:
            raise ValidationError('Campo obligatorio')
        if not isinstance(stock, int):
            raise ValidationError('Debe ingresar un número entero' )
        return stock
    

    def clean_proveedores(self):
        proveedor = self.cleaned_data.get('proveedor')
        if not proveedor:
            raise ValidationError('Campo obligatorio')
        return proveedor




class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['razon_social', 'nombre', 'apellido', 'dni']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['razon_social'].widget.attrs.update({'class': 'form-control'})
        self.fields['nombre'].widget.attrs.update({'class': 'form-control'})
        self.fields['apellido'].widget.attrs.update({'class':'form-control'})
        self.fields['dni'].widget.attrs.update({'class':'form-control'})


    def clean_razon_social(self):
        rsocial = self.cleaned_data.get('razon_social')
        if not rsocial:
            raise ValidationError('Campo obligatorio')
        return rsocial
    

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise ValidationError('Campo obligatorio')
        return nombre
        
    
    def clean_apellido(self):
        apellido = self.cleaned_data.get('apellido')
        if not apellido:
            raise ValidationError('Campo obligatorio')
        return apellido
    

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if not dni:
            raise ValidationError('Campo obligatorio')
        if not isinstance(dni, int):
            raise ValidationError('Solo puede ingresar numeros')
        if len(str(dni)) not in [7,8]:
            raise ValidationError('Debe ingresar entre 7 y 8 caracteres numéricos')
        return dni
    

    