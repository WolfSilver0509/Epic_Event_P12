from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from epic.models import Client
from epic.serializers import ClientSerializer


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all()

