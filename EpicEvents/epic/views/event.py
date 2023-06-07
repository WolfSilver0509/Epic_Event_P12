from rest_framework.viewsets import ModelViewSet

from epic.models import Event
from epic.serializers import EventSerializer

class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.all()