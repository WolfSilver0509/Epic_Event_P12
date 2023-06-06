from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('GESTION', 'Gestion'),
        ('VENTES', 'Vente'),
        ('SUPPORT', 'Support'),
    )
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
