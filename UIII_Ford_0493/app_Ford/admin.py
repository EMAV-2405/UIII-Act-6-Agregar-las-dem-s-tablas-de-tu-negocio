# app_Ford/admin.py
from django.contrib import admin
from .models import Empleado, Vehiculo, Venta

# Registrar los modelos para que aparezcan en el panel de admin
admin.site.register(Empleado)
admin.site.register(Vehiculo)
admin.site.register(Venta)
