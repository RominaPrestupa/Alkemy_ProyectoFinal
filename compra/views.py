from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from compra.models import Producto, Proveedor
from django.contrib import messages
#from .forms import ProductoForm, ProveedorForm


#LEER
# vista para el listado productos:
@login_required
def listar_productos(request):
    mostrar_navbar = True
    productos = Producto.objects.all()
    return render(request, 'compra/listado-productos.html', {'productos':productos})


# vista para el listado proveedores:
@login_required
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'compra/listado-proveedores.html', {'proveedores': proveedores})
    

#CREATE
@login_required
@permission_required('compra.add_producto', raise_exception=True)
def agregar_producto(request):
        if request.method == "POST":
            nombre = request.POST.get('nombre_producto')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')
            id_proveedor = request.POST.get('id_proveedor')

            proveedor = get_object_or_404(Proveedor, id = id_proveedor)
            
            producto = Producto.objects.create(
                 nombre_producto = nombre, 
                 precio = precio, 
                 stock_actual = stock, 
                 proveedor = proveedor)
            return redirect('listado-productos') 
        proveedores = Proveedor.objects.all()
        return render(request,'compra/form-productos.html', {'proveedores': proveedores})
    

@login_required
@permission_required('compra.add_proveedor', raise_exception=True)
def agregar_proveedor(request):
        if request.method == "POST":
            razon_social = request.POST.get('Razon Social')
            nombre = request.POST.get('Nombre')
            apellido = request.POST.get('Apellido')
            documento_identidad = request.POST.get('DNI')
            proveedor = Proveedor.objects.create(razon_social = razon_social, nombre = nombre, apellido = apellido, dni = documento_identidad)
            return redirect('listado-proveedores') 
        return render(request,'compra/form-proveedores.html')

