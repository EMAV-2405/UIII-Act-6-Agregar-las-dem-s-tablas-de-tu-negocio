# app_Ford/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ==========================================
    # URLS PRINCIPALES
    # ==========================================
    path('', views.inicio_ford, name='inicio'),

    # ==========================================
    # URLS CRUD DE VEHÍCULO
    # ==========================================
    path('vehiculos/agregar/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculos/ver/', views.ver_vehiculos, name='ver_vehiculos'),
    # KEEPING THIS ONE, as the view function exists:
    path('vehiculos/actualizar/<int:id>/', views.actualizar_vehiculo, name='actualizar_vehiculo'),
    # REMOVING THIS ONE, as 'views.realizar_actualizacion_vehiculo' does NOT exist:
    # path('vehiculos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_vehiculo, name='realizar_actualizacion_vehiculo'),
    path('vehiculos/borrar/<int:id>/', views.borrar_vehiculo, name='borrar_vehiculo'),

    # ==========================================
    # URLS CRUD DE EMPLEADO
    # ==========================================
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('empleados/ver/', views.ver_empleados, name='ver_empleados'),
    # KEEPING THIS ONE:
    path('empleados/actualizar/<int:id>/', views.actualizar_empleado, name='actualizar_empleado'),
    # REMOVING THIS ONE:
    # path('empleados/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_empleado, name='realizar_actualizacion_empleado'),
    path('empleados/borrar/<int:id>/', views.borrar_empleado, name='borrar_empleado'),

    # ==========================================
    # URLS CRUD DE VENTA
    # ==========================================
    path('ventas/registrar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/ver/', views.ver_ventas, name='ver_ventas'), 
    # KEEPING THIS ONE:
    path('ventas/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    # REMOVING THIS ONE:
    # path('ventas/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('ventas/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),
    # REMOVED DUPLICATE: path('ventas/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),

    # ==========================================
    # URLS CRUD DE CLIENTE (NUEVAS)
    # ==========================================
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/ver/', views.ver_clientes, name='ver_clientes'),
    # KEEPING THIS ONE:
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    # REMOVING THIS ONE:
    # path('clientes/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # ==========================================
    # URLS CRUD DE PROVEEDOR (NUEVAS)
    # ==========================================
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/ver/', views.ver_proveedores, name='ver_proveedores'),
    # KEEPING THIS ONE:
    path('proveedores/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    # REMOVING THIS ONE:
    # path('proveedores/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedores/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # ==========================================
    # URLS CRUD DE SERVICIOS (NUEVAS)
    # ==========================================
    path('servicios/agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('servicios/ver/', views.ver_servicios, name='ver_servicios'),
    # KEEPING THIS ONE:
    path('servicios/actualizar/<int:id>/', views.actualizar_servicio, name='actualizar_servicio'),
    # REMOVING THIS ONE:
    # path('servicios/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_servicio, name='realizar_actualizacion_servicio'),
    path('servicios/borrar/<int:id>/', views.borrar_servicio, name='borrar_servicio'),
]