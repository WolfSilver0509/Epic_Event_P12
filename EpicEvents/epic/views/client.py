from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from epic.permissions import SalesOrGestion

from epic.models import Client
from epic.serializers import ClientSerializer

from rest_framework import filters

class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer

    permission_classes = [IsAuthenticated, SalesOrGestion]

    #Rajout des filtres pour rechercher par des API Endpoint /////////////////////////////////
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']

    def perform_create(self, serializer):
        serializer.save(contact_ventes=self.request.user)

    def perform_update(self, serializer):
        serializer.save(contact_ventes=self.request.user)

    def get_queryset(self):
        return Client.objects.all()  # filter(contact_ventes = self.request.user)
