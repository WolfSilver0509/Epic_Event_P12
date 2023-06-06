from django.db import models

from authentification.models import User

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    contact_ventes = models.ForeignKey('authentification.User', on_delete=models.SET_NULL, null=True, related_name='client_contact_ventes')


class Contract(models.Model):
    contact_ventes = models.ForeignKey('authentification.User', on_delete=models.SET_NULL, null=True,related_name='contract_contact_ventes')
    client = models.ForeignKey('Client', on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()



class Event(models.Model):
    EVENT_STATUS_CHOICES = (
        ('A venir', 'A venir'),
        ('En cours', 'En cours'),
        ('Terminer', 'Terminer'),
    )

    contract = models.ForeignKey('Contract', on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey('authentification.User', on_delete=models.SET_NULL, null=True, related_name='event_support_contact')
    event_status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    notes = models.TextField()