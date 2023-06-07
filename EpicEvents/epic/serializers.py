from rest_framework import serializers
from .models import Client, Contract, Event

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ContractSerializer(serializers.ModelSerializer):
    payment_due = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = Contract
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    event_date = serializers.DateTimeField(format='%Y-%m-%d')
    class Meta:
        model = Event
        fields = '__all__'
