from rest_framework import serializers
from .models import Cliente, Medicamento, Pedido

class ClienteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Cliente
    fields = '__all__'
    read_only_fields = ('created_at',)

class MedicamentoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Medicamento
    fields = '__all__'
    read_only_fields = ('created_at',)

class PedidoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pedido
    fields = '__all__'
    read_only_fields = ('created_at',)