# app_Ford/models.py
from django.db import models

# ==========================================
# MODELO: EMPLEADO
# ==========================================
class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fecha_contratacion = models.DateField(blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self):  
        return f"{self.nombre} {self.apellido}"  

# ==========================================
# MODELO: VEHÍCULO
# ==========================================
class Vehiculo(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.PositiveIntegerField()
    color = models.CharField(max_length=50, blank=True, null=True)
    numero_serie = models.CharField(max_length=100, unique=True)
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    cantidad_disponible = models.PositiveIntegerField(default=1)
    
    def __str__(self):  
        return f"{self.marca} {self.modelo} ({self.anio})"  

# ==========================================
# MODELO: VENTA
# ==========================================
class Venta(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='ventas')
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas')
    cliente_nombre = models.CharField(max_length=150)
    cliente_telefono = models.CharField(max_length=50, blank=True, null=True)
    fecha_venta = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    metodo_pago = models.CharField(max_length=50, blank=True, null=True)
    folio = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):  
        return f"Venta {self.folio or self.id}"

# ==========================================
# MODELO: CLIENTE (NUEVO)
# ==========================================
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    fecha_registro = models.DateField(auto_now_add=True) # Se asigna la fecha actual al crear

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==========================================
# MODELO: PROVEEDOR (NUEVO)
# ==========================================
class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=200)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    producto = models.CharField(max_length=100, blank=True, null=True) # Producto o servicio que ofrece

    def __str__(self):
        return self.nombre_proveedor

# ==========================================
# MODELO: SERVICIO MANTENIMIENTO (NUEVO)
# ==========================================
class ServicioMantenimiento(models.Model):
    # Relaciones (Foreign Keys)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE, related_name='servicios')
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='servicios')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True, related_name='servicios')

    # Campos de la tabla
    tipo_servicio = models.CharField(max_length=150)
    fecha_servicio = models.DateField()
    costo_servicio = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Servicio de '{self.tipo_servicio}' para {self.vehiculo}"