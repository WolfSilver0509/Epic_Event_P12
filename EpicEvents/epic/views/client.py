from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from epic.permissions import SalesOrGestion

from epic.models import Client
from epic.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer

    permission_classes = [IsAuthenticated, SalesOrGestion]

    def perform_create(self, serializer):
        serializer.save(contact_ventes=self.request.user)

    def perform_update(self, serializer):
        serializer.save(contact_ventes=self.request.user)


    def get_queryset(self):
        return Client.objects.all()#filter(contact_ventes = self.request.user)

