from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from compra.models import Producto, Proveedor
#from django.contrib import messages
from .forms import ProductoForm, ProveedorForm


#LEER
# vista para el listado productos:
@login_required
def listar_productos(request):
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
            producto_form = ProductoForm(request.POST)
            if producto_form.is_valid():
                producto_form.save(commit=True)
                return redirect('listado-productos')
        else:
            producto_form = ProductoForm()
        return render(request, 'compra/form-productos.html', {'producto_form': producto_form})

    

@login_required
@permission_required('compra.add_proveedor', raise_exception=True)
def agregar_proveedor(request):
    if request.method == "POST":
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save(commit=True)
            return redirect('listado-proveedores')
    else:
        proveedor_form = ProveedorForm()
    return render(request, 'compra/form-proveedores.html', {'proveedor_form':proveedor_form})

