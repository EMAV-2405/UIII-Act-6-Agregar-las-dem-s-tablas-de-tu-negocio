# app_Ford/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehiculo, Empleado, Venta, Cliente, Proveedor, ServicioMantenimiento
from datetime import date 
# Se puede usar para mostrar mensajes de error, aunque en este ejemplo
# pasaremos el error en el contexto.
# from django.contrib import messages 

# ==========================================
# VISTAS PRINCIPALES
# ==========================================

def inicio_ford(request):
    """
    Renderiza la página de inicio.
    """
    return render(request, 'inicio.html')

# ==========================================
# VISTAS CRUD DE VEHÍCULO (Refactorizadas)
# ==========================================

def agregar_vehiculo(request):
    if request.method == "POST":
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        # Es crucial validar y convertir tipos de datos si no son cadenas.
        # Por ejemplo, para anio y precio:
        try:
            anio = int(request.POST.get('anio'))
        except (ValueError, TypeError):
            anio = None # O manejar el error de otra forma, e.g., messages.error()
        try:
            precio = float(request.POST.get('precio'))
        except (ValueError, TypeError):
            precio = None # O manejar el error
        try:
            cantidad = int(request.POST.get('cantidad_disponible'))
        except (ValueError, TypeError):
            cantidad = 0 # O manejar el error
        
        numero_serie = request.POST.get('numero_serie')
        color = request.POST.get('color')

        Vehiculo.objects.create(
            marca=marca,
            modelo=modelo,
            anio=anio,
            precio=precio,
            cantidad_disponible=cantidad,
            numero_serie=numero_serie,
            color=color
        )
        return redirect('ver_vehiculos') 
    
    return render(request, 'vehiculos/agregar_vehiculo.html')


def ver_vehiculos(request):
    todos_los_vehiculos = Vehiculo.objects.all()
    contexto = {
        'vehiculos': todos_los_vehiculos
    }
    return render(request, 'vehiculos/ver_vehiculos.html', contexto)


def actualizar_vehiculo(request, id):
    """
    Vista fusionada:
    - GET: Muestra el formulario de actualización con datos existentes.
    - POST: Procesa los datos del formulario y guarda los cambios.
    """
    vehiculo_a_actualizar = get_object_or_404(Vehiculo, id=id)
    
    if request.method == "POST":
        vehiculo_a_actualizar.marca = request.POST.get('marca')
        vehiculo_a_actualizar.modelo = request.POST.get('modelo')
        
        # Validación y conversión para campos numéricos/otros tipos
        try:
            vehiculo_a_actualizar.anio = int(request.POST.get('anio'))
        except (ValueError, TypeError):
            vehiculo_a_actualizar.anio = None # O mantener el valor anterior o dar un error
            
        try:
            vehiculo_a_actualizar.precio = float(request.POST.get('precio'))
        except (ValueError, TypeError):
            vehiculo_a_actualizar.precio = None # O mantener el valor anterior o dar un error
            
        try:
            vehiculo_a_actualizar.cantidad_disponible = int(request.POST.get('cantidad_disponible'))
        except (ValueError, TypeError):
            vehiculo_a_actualizar.cantidad_disponible = 0 # O mantener el valor anterior o dar un error
            
        vehiculo_a_actualizar.numero_serie = request.POST.get('numero_serie')
        vehiculo_a_actualizar.color = request.POST.get('color')
        
        vehiculo_a_actualizar.save()
        return redirect('ver_vehiculos')
    
    # Si es GET, muestra el formulario de actualización
    contexto = {
        'vehiculo': vehiculo_a_actualizar
    }
    return render(request, 'vehiculos/actualizar_vehiculo.html', contexto)


def borrar_vehiculo(request, id):
    vehiculo_a_borrar = get_object_or_404(Vehiculo, id=id)
    vehiculo_a_borrar.delete()
    
    return redirect('ver_vehiculos')

# ==========================================
# VISTAS CRUD DE EMPLEADO (Refactorizadas)
# ==========================================

def agregar_empleado(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        puesto = request.POST.get('puesto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        
        fecha_contratacion_str = request.POST.get('fecha_contratacion')
        fecha_contratacion = None
        if fecha_contratacion_str:
            try:
                # Asumiendo formato YYYY-MM-DD del input type="date"
                fecha_contratacion = date.fromisoformat(fecha_contratacion_str)
            except ValueError:
                pass # Manejar el error si la fecha no es válida
                
        try:
            salario = float(request.POST.get('salario'))
        except (ValueError, TypeError):
            salario = None

        Empleado.objects.create(
            nombre=nombre,
            apellido=apellido,
            puesto=puesto,
            telefono=telefono,
            email=email,
            fecha_contratacion=fecha_contratacion,
            salario=salario
        )
        return redirect('ver_empleados')

    return render(request, 'empleados/agregar_empleado.html')

def ver_empleados(request):
    todos_los_empleados = Empleado.objects.all()
    contexto = {
        'empleados': todos_los_empleados
    }
    return render(request, 'empleados/ver_empleados.html', contexto)

def actualizar_empleado(request, id):
    """
    Vista fusionada:
    - GET: Muestra el formulario de actualización.
    - POST: Procesa los datos y guarda los cambios.
    """
    empleado_a_actualizar = get_object_or_404(Empleado, id=id)
    
    if request.method == "POST":
        empleado_a_actualizar.nombre = request.POST.get('nombre')
        empleado_a_actualizar.apellido = request.POST.get('apellido')
        empleado_a_actualizar.puesto = request.POST.get('puesto')
        empleado_a_actualizar.telefono = request.POST.get('telefono')
        empleado_a_actualizar.email = request.POST.get('email')
        
        fecha_contratacion_str = request.POST.get('fecha_contratacion')
        if fecha_contratacion_str:
            try:
                empleado_a_actualizar.fecha_contratacion = date.fromisoformat(fecha_contratacion_str)
            except ValueError:
                empleado_a_actualizar.fecha_contratacion = None # O mantener el valor anterior
        else:
            empleado_a_actualizar.fecha_contratacion = None # Si el campo viene vacío
        
        salario_str = request.POST.get('salario')
        try:
            empleado_a_actualizar.salario = float(salario_str)
        except (ValueError, TypeError):
            empleado_a_actualizar.salario = None # O mantener el valor anterior

        empleado_a_actualizar.save()
        return redirect('ver_empleados')
    
    # Si es GET, muestra el formulario
    contexto = {
        'empleado': empleado_a_actualizar
    }
    return render(request, 'empleados/actualizar_empleado.html', contexto)

def borrar_empleado(request, id):
    empleado_a_borrar = get_object_or_404(Empleado, id=id)
    empleado_a_borrar.delete()
    return redirect('ver_empleados')


# ==========================================
# VISTAS CRUD DE VENTA (Refactorizadas y con validación de stock)
# ==========================================

def agregar_venta(request):
    vehiculos = Vehiculo.objects.all() 
    empleados = Empleado.objects.all() 
    contexto = {
        'vehiculos': vehiculos,
        'empleados': empleados
    }

    if request.method == "POST":
        vehiculo_id = request.POST.get('vehiculo')
        empleado_id = request.POST.get('empleado')
        
        # --- Validación de Stock ---
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        if vehiculo.cantidad_disponible <= 0:
            # Si no hay stock, volvemos al formulario con un mensaje de error
            contexto['error'] = f"No hay stock disponible para el vehículo: {vehiculo.marca} {vehiculo.modelo}."
            return render(request, 'ventas/agregar_venta.html', contexto)
        
        empleado = get_object_or_404(Empleado, id=empleado_id) if empleado_id else None 

        try:
            total = float(request.POST.get('total'))
        except (ValueError, TypeError):
            total = 0.0 # O manejar el error

        Venta.objects.create(
            vehiculo=vehiculo,
            empleado=empleado,
            cliente_nombre=request.POST.get('cliente_nombre'),
            cliente_telefono=request.POST.get('cliente_telefono'),
            total=total,
            metodo_pago=request.POST.get('metodo_pago'),
            folio=request.POST.get('folio'),
            fecha_venta=date.today() 
        )
        
        # Restar del stock (ahora sabemos que es seguro)
        vehiculo.cantidad_disponible -= 1
        vehiculo.save()

        return redirect('ver_ventas')
    
    # Si es GET, muestra el formulario
    return render(request, 'ventas/agregar_venta.html', contexto)


def ver_ventas(request):
    todas_las_ventas = Venta.objects.select_related('vehiculo', 'empleado').all()
    contexto = {
        'ventas': todas_las_ventas
    }
    return render(request, 'ventas/ver_ventas.html', contexto)


def actualizar_venta(request, id):
    """
    Vista fusionada:
    - GET: Muestra el formulario de actualización.
    - POST: Procesa los datos y guarda los cambios, validando stock.
    """
    venta_a_actualizar = get_object_or_404(Venta, id=id)
    vehiculos = Vehiculo.objects.all()
    empleados = Empleado.objects.all()
    
    contexto = {
        'venta': venta_a_actualizar,
        'vehiculos': vehiculos,
        'empleados': empleados
    }

    if request.method == "POST":
        vehiculo_anterior = venta_a_actualizar.vehiculo
        vehiculo_nuevo_id = request.POST.get('vehiculo')
        vehiculo_nuevo = get_object_or_404(Vehiculo, id=vehiculo_nuevo_id)

        # --- Validación de Stock si el vehículo cambia ---
        if vehiculo_anterior.id != vehiculo_nuevo.id:
            if vehiculo_nuevo.cantidad_disponible <= 0:
                # Si no hay stock del nuevo vehículo, volvemos al formulario con error
                contexto['error'] = f"No hay stock disponible para el nuevo vehículo: {vehiculo_nuevo.marca} {vehiculo_nuevo.modelo}."
                return render(request, 'ventas/actualizar_venta.html', contexto)
            
            # Actualizar stock
            vehiculo_anterior.cantidad_disponible += 1 
            vehiculo_anterior.save()
            vehiculo_nuevo.cantidad_disponible -= 1 
            vehiculo_nuevo.save()

        # Actualizar la venta
        venta_a_actualizar.vehiculo = vehiculo_nuevo
        
        empleado_id = request.POST.get('empleado')
        venta_a_actualizar.empleado = get_object_or_404(Empleado, id=empleado_id) if empleado_id else None
        
        venta_a_actualizar.cliente_nombre = request.POST.get('cliente_nombre')
        venta_a_actualizar.cliente_telefono = request.POST.get('cliente_telefono')
        
        try:
            venta_a_actualizar.total = float(request.POST.get('total'))
        except (ValueError, TypeError):
            venta_a_actualizar.total = 0.0 # O mantener el valor anterior
            
        venta_a_actualizar.metodo_pago = request.POST.get('metodo_pago')
        venta_a_actualizar.folio = request.POST.get('folio')
        venta_a_actualizar.save()

        return redirect('ver_ventas')
    
    # Si es GET, muestra el formulario
    return render(request, 'ventas/actualizar_venta.html', contexto)


def borrar_venta(request, id):
    venta_a_borrar = get_object_or_404(Venta, id=id)
    vehiculo_vendido = venta_a_borrar.vehiculo 

    venta_a_borrar.delete()
    
    # Devolver el vehículo al stock
    vehiculo_vendido.cantidad_disponible += 1
    vehiculo_vendido.save()
    
    return redirect('ver_ventas')

# ==========================================
# VISTAS CRUD DE CLIENTE (Refactorizadas)
# ==========================================

def agregar_cliente(request):
    if request.method == "POST":
        Cliente.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            correo_electronico=request.POST.get('correo_electronico'),
            telefono=request.POST.get('telefono')
        )
        return redirect('ver_clientes')
    return render(request, 'clientes/agregar_cliente.html')

def ver_clientes(request):
    todos_los_clientes = Cliente.objects.all()
    contexto = {
        'clientes': todos_los_clientes
    }
    return render(request, 'clientes/ver_clientes.html', contexto)

def actualizar_cliente(request, id):
    """
    Vista fusionada:
    - GET: Muestra el formulario de actualización.
    - POST: Procesa los datos y guarda los cambios.
    """
    cliente_a_actualizar = get_object_or_404(Cliente, id=id)
    
    if request.method == "POST":
        cliente_a_actualizar.nombre = request.POST.get('nombre')
        cliente_a_actualizar.apellido = request.POST.get('apellido')
        cliente_a_actualizar.correo_electronico = request.POST.get('correo_electronico')
        cliente_a_actualizar.telefono = request.POST.get('telefono')
        cliente_a_actualizar.save()
        return redirect('ver_clientes')
    
    # Si es GET
    contexto = {
        'cliente': cliente_a_actualizar
    }
    return render(request, 'clientes/actualizar_cliente.html', contexto)

def borrar_cliente(request, id):
    cliente_a_borrar = get_object_or_404(Cliente, id=id)
    cliente_a_borrar.delete()
    return redirect('ver_clientes')

# ==========================================
# VISTAS CRUD DE PROVEEDOR (Refactorizadas)
# ==========================================

def agregar_proveedor(request):
    if request.method == "POST":
        Proveedor.objects.create(
            nombre_proveedor=request.POST.get('nombre_proveedor'),
            telefono=request.POST.get('telefono'),
            direccion=request.POST.get('direccion'),
            email=request.POST.get('email'),
            producto=request.POST.get('producto')
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedores/agregar_proveedor.html')

def ver_proveedores(request):
    todos_los_proveedores = Proveedor.objects.all()
    contexto = {
        'proveedores': todos_los_proveedores
    }
    return render(request, 'proveedores/ver_proveedores.html', contexto)

def actualizar_proveedor(request, id):
    """
    Vista fusionada:
    - GET: Muestra el formulario de actualización.
    - POST: Procesa los datos y guarda los cambios.
    """
    proveedor_a_actualizar = get_object_or_404(Proveedor, id=id)
    
    if request.method == "POST":
        proveedor_a_actualizar.nombre_proveedor = request.POST.get('nombre_proveedor')
        proveedor_a_actualizar.telefono = request.POST.get('telefono')
        proveedor_a_actualizar.direccion = request.POST.get('direccion')
        proveedor_a_actualizar.email = request.POST.get('email')
        proveedor_a_actualizar.producto = request.POST.get('producto')
        proveedor_a_actualizar.save()
        return redirect('ver_proveedores')
    
    # Si es GET
    contexto = {
        'proveedor': proveedor_a_actualizar
    }
    return render(request, 'proveedores/actualizar_proveedor.html', contexto)

def borrar_proveedor(request, id):
    proveedor_a_borrar = get_object_or_404(Proveedor, id=id)
    proveedor_a_borrar.delete()
    return redirect('ver_proveedores')

# ==========================================
# VISTAS CRUD DE SERVICIO MANTENIMIENTO (Refactorizadas)
# ==========================================

def agregar_servicio(request):
    vehiculos = Vehiculo.objects.all()
    clientes = Cliente.objects.all()
    proveedores = Proveedor.objects.all()
    
    if request.method == "POST":
        vehiculo_id = request.POST.get('vehiculo')
        cliente_id = request.POST.get('cliente')
        proveedor_id = request.POST.get('proveedor')
        
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        cliente = get_object_or_404(Cliente, id=cliente_id) if cliente_id else None
        proveedor = get_object_or_404(Proveedor, id=proveedor_id) if proveedor_id else None

        try:
            costo_servicio = float(request.POST.get('costo_servicio'))
        except (ValueError, TypeError):
            costo_servicio = 0.0 # O manejar el error

        fecha_servicio_str = request.POST.get('fecha_servicio')
        fecha_servicio = None
        if fecha_servicio_str:
            try:
                fecha_servicio = date.fromisoformat(fecha_servicio_str)
            except ValueError:
                pass # Manejar el error si la fecha no es válida


        ServicioMantenimiento.objects.create(
            vehiculo=vehiculo,
            cliente=cliente,
            proveedor=proveedor,
            tipo_servicio=request.POST.get('tipo_servicio'),
            fecha_servicio=fecha_servicio,
            costo_servicio=costo_servicio
        )
        return redirect('ver_servicios')
        
    contexto = {
        'vehiculos': vehiculos,
        'clientes': clientes,
        'proveedores': proveedores
    }
    return render(request, 'servicios/agregar_servicio.html', contexto)

def ver_servicios(request):
    todos_los_servicios = ServicioMantenimiento.objects.select_related('vehiculo', 'cliente', 'proveedor').all()
    contexto = {
        'servicios': todos_los_servicios
    }
    return render(request, 'servicios/ver_servicios.html', contexto)


def actualizar_servicio(request, id):
    """
    Vista para actualizar un servicio de mantenimiento existente.
    """
    servicio_a_actualizar = get_object_or_404(ServicioMantenimiento, id=id)
    vehiculos = Vehiculo.objects.all()
    clientes = Cliente.objects.all()
    proveedores = Proveedor.objects.all()

    contexto = {
        'servicio': servicio_a_actualizar,
        'vehiculos': vehiculos,
        'clientes': clientes,
        'proveedores': proveedores
    }

    if request.method == "POST":
        vehiculo_id = request.POST.get('vehiculo')
        cliente_id = request.POST.get('cliente')
        proveedor_id = request.POST.get('proveedor')

        servicio_a_actualizar.vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        servicio_a_actualizar.cliente = get_object_or_404(Cliente, id=cliente_id) if cliente_id else None
        servicio_a_actualizar.proveedor = get_object_or_404(Proveedor, id=proveedor_id) if proveedor_id else None
        servicio_a_actualizar.tipo_servicio = request.POST.get('tipo_servicio')
        
        fecha_servicio_str = request.POST.get('fecha_servicio')
        if fecha_servicio_str:
            try:
                servicio_a_actualizar.fecha_servicio = date.fromisoformat(fecha_servicio_str)
            except ValueError:
                servicio_a_actualizar.fecha_servicio = None # O manejar el error
        else:
            servicio_a_actualizar.fecha_servicio = None # Si el campo viene vacío

        try:
            servicio_a_actualizar.costo_servicio = float(request.POST.get('costo_servicio'))
        except (ValueError, TypeError):
            servicio_a_actualizar.costo_servicio = 0.0 # O mantener el valor anterior

        servicio_a_actualizar.save()
        return redirect('ver_servicios')

    return render(request, 'servicios/actualizar_servicio.html', contexto)


def borrar_servicio(request, id):
    servicio_a_borrar = get_object_or_404(ServicioMantenimiento, id=id)
    servicio_a_borrar.delete()
    return redirect('ver_servicios')