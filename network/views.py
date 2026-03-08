from rest_framework import viewsets
from .permissions import IsActiveStaffUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import ElectronicsNetwork
from .serializers import ElectronicsNetworkSerializer
from .filters import ElectronicsNetworkFilter


class ElectronicsNetworkViewSet(viewsets.ModelViewSet):
    """
    CRUD для звена сети.
    Запрещено обновлять `debt` и `level`.
    Фильтрация: страна, город, уровень.
    """
    queryset = ElectronicsNetwork.objects.all()
    serializer_class = ElectronicsNetworkSerializer
    permission_classes = [IsActiveStaffUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = ElectronicsNetworkFilter  # Подключаем фильтр