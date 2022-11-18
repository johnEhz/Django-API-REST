from django.db import models

# Create your models here.
class Medicamento(models.Model):
  nombre = models.CharField(max_length=150)
  marca = models.CharField(max_length=150)
  MED_TYPES = (
    ('Analgésico', 'Analgésico'),
    ('Anestésico', 'Anestésico'),
    ('Antibiótico', 'Antibiótico'),
    ('Anticonceptivo', 'Anticonceptivo'),
    ('Ansiolítico', 'Ansiolítico'),
  )
  tipo = models.CharField(max_length=50, choices=MED_TYPES)
  formula = models.BinaryField(null=False)
  precio = models.IntegerField(null=False)
  cantidad = models.IntegerField(default=0)

  def __str__(self):
    return "%s - (%s), %s" % (self.nombre, self.marca, self.tipo)

class Cliente(models.Model):
  dni = models.IntegerField(primary_key=True)
  nombre = models.CharField(max_length=150, null=False)
  email = models.EmailField(max_length=100)
  telefono = models.IntegerField()
  edad = models.IntegerField(null=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return "%s - %s" % (self.dni, self.nombre)

class Pedido(models.Model):
  client = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=False)
  medicine = models.ForeignKey(Medicamento, on_delete=models.CASCADE, null=False)
  cantidad = models.IntegerField(null=False)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return "%s - %s por: $ %s" % (self.client.dni, self.medidine.nombre, self.medicine.precio*self.cantidad)