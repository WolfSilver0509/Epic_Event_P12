from rest_framework.viewsets import ModelViewSet

from epic.models import Contract
from epic.serializers import ContractSerializer

class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer

    def get_queryset(self):
        return Contract.objects.all()