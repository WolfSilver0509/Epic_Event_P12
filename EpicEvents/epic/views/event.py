from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from epic.models import Event
from epic.serializers import EventSerializer
from epic.permissions import SupportOrSalesOrGestion


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated, SupportOrSalesOrGestion]

    def perform_create(self, serializer):
        contrat = serializer.validated_data.get("contract")
        if contrat.contact_ventes == self.request.user:
            if contrat.event_set.exists():
                raise PermissionDenied("Un evenement est déja associé à ce contrat !")
            elif contrat.status == False:
                raise PermissionDenied("Ce contrat n'est pas signé !")
            else:
                serializer.save()
        else:
            raise PermissionDenied(
                "Vous n'êtes pas le contact ventes associé à ce contrat."
            )

    def get_queryset(self):
        return Event.objects.all()
