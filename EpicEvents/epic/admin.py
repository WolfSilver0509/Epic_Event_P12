from django.contrib import admin
from .models import Client, Contract, Event

# Chaque modèle (Client, Contract, Event) est enregistré dans
# l'interface d'administration en utilisant le décorateur admin.register.
# Le décorateur admin.register prend en paramètre le modèle à enregistrer.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name']
    search_fields = ['first_name', 'last_name', 'email', 'company_name']

@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ['contact_ventes', 'client', 'status', 'amount', 'payment_due']
    search_fields = ['contact_ventes__email', 'client__first_name', 'client__last_name']
    list_filter = ['status']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['contract', 'event_date', 'event_status', 'attendees']
    search_fields = ['contract__client__first_name', 'contract__client__last_name']
    list_filter = ['event_status']
