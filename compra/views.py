from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from compra.models import Producto, Proveedor

""" 
def home(request):
    mostrar_navbar = True
    return render(request, 'compra/index.html')
 """

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
@permission_required('compra.add_proveedor', raise_exception=True)
def agregar_proveedor(request):
        if request.method == "POST":
            print(request)
            razon_social = request.POST.get('Razon Social')
            nombre = request.POST.get('Nombre')
            apellido = request.POST.get('Apellido')
            documento_identidad = request.POST.get('DNI')
            proveedor = Proveedor.objects.create(razon_social = razon_social, nombre = nombre, apellido = apellido, dni = documento_identidad)
            return redirect('listado-proveedores') 
        return render(request,'compra/form-proveedores.html') 
    

@login_required
@permission_required('compra.add_producto', raise_exception=True)
def agregar_producto(request):
        if request.method == "POST":
            nombre = request.POST.get('Nombre Producto')
            precio = request.POST.get('Precio')
            stock = request.POST.get('Stock')
            proveedor = request.POST.get('Proveedor')

            proveedor = get_object_or_404(Proveedor, razon_social = proveedor)
            
            producto = Producto.objects.create(
                 nombre_producto = nombre, 
                 precio = precio, 
                 stock_actual = stock, 
                 proveedor = proveedor)
            return redirect('listado-productos')
        return render(request,'compra/form-productos.html') 
