from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from epic.models import Event
from epic.serializers import EventSerializer

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.all()