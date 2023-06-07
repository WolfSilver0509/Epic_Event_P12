from rest_framework.viewsets import ModelViewSet

from epic.models import Client
from epic.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()

