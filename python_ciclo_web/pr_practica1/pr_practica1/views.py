from django.http import HttpResponse
from django.shortcuts import render

# Función para la URL /ayuda
def funcion_ayuda(request):
    return HttpResponse("<h2>Centro de Ayuda</h2><p>Esta es la página de ayuda del proyecto pr_practica1.</p>")

# Función para la URL /productos
def funcion_productos(request):
    # Lista de 5 productos
    lista_productos = [
        {'codigo': 'P001', 'nombre': 'Teclado Mecánico', 'cantidad': 15, 'precio': 45.00},
        {'codigo': 'P002', 'nombre': 'Mouse Inalámbrico', 'cantidad': 30, 'precio': 22.50},
        {'codigo': 'P003', 'nombre': 'Monitor 24 pulgadas', 'cantidad': 8, 'precio': 150.00},
        {'codigo': 'P004', 'nombre': 'Auriculares Gamer', 'cantidad': 12, 'precio': 35.99},
        {'codigo': 'P005', 'nombre': 'Alfombrilla XL', 'cantidad': 50, 'precio': 12.00},
    ]
    
    return render(request, 'productos.html', {'productos': lista_productos})