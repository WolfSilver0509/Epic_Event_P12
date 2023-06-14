from rest_framework import serializers
from .models import Client, Contract, Event
from authentification.models import User


class ContactVenteSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = User.objects.filter(role="VENTE")
        return queryset


class ContactSupportSerializer(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        queryset = User.objects.filter(role="SUPPORT")
        return queryset


class ClientSerializer(serializers.ModelSerializer):
    contact_ventes = ContactVenteSerializer(required=False)

    class Meta:
        model = Client
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    contact_ventes = ContactVenteSerializer(required=False)
    payment_due = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Contract
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    support_contact = ContactSupportSerializer()
    event_date = serializers.DateTimeField(format="%Y-%m-%d")

    class Meta:
        model = Event
        fields = "__all__"
