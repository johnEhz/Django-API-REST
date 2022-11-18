from projects.models import Medicamento, Cliente, Pedido
from rest_framework import viewsets, permissions
from .serializers import ClienteSerializer, MedicamentoSerializer, PedidoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
  queryset = Cliente.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = ClienteSerializer

class MedicamentoViewSet(viewsets.ModelViewSet):
  queryset = Medicamento.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = MedicamentoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
  queryset = Pedido.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = PedidoSerializer