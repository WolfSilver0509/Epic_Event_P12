from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import serializers

from epic.models import Contract
from epic.serializers import ContractSerializer
from epic.permissions import ViewOrUpdateSales


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer

    permission_classes = [IsAuthenticated, ViewOrUpdateSales]

    def perform_create(self,serializer):
        client = serializer.validated_data.get("client")
        if client.contact_ventes == self.request.user:
            if client.contract_set.filter(status = False):
                raise PermissionDenied("Ce client à un contrat en attente de signature!")
            else:
                serializer.save(contact_ventes = self.request.user)
        else:
            raise PermissionDenied("Vous n'êtes pas le contact ventes associé à ce client.") #serializers.ValidationError("Vous n'êtes pas le contact ventes associé à ce client.")


    def get_queryset(self):
        return Contract.objects.filter(contact_ventes = self.request.user)