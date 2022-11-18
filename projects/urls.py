from rest_framework import routers
from .api import ClienteViewSet, MedicamentoViewSet, PedidoViewSet

router = routers.DefaultRouter()

router.register('api/clients', ClienteViewSet, 'client')
router.register('api/medicines', MedicamentoViewSet, 'medicine')
router.register('api/orders', PedidoViewSet, 'order')

urlpatterns = router.urls
