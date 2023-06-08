from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from epic.models import Contract
from epic.serializers import ContractSerializer

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contract.objects.all()