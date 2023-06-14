from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class ManagerUser(BaseUserManager):
    def create_user(self, email, first_name, last_name, role, password=None):
        if not email:
            raise ValueError("Vous devez entrer un email")
        if not first_name:
            raise ValueError("Vous devez entrer un prénom")
        if not last_name:
            raise ValueError("Vous devez entrer un nom")
        if not role:
            raise ValueError("Vous devez entrer un rôle")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractUser):
    ROLE_CHOICES = (
        ("GESTION", "Gestion"),
        ("VENTE", "Vente"),
        ("SUPPORT", "Support"),
    )
    username = None
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True, blank=True)
    email = models.EmailField(unique=True, max_length=255, blank=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = ManagerUser()
