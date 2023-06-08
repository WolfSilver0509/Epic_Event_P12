from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import User

class UserAdmin(BaseUserAdmin):
    # Définir l'ordre des champs dans la liste des utilisateurs
    ordering = ['email']

    # Définir les champs d'affichage dans la liste des utilisateurs
    list_display = ['email', 'first_name', 'last_name', 'role', 'is_staff']

    # Définir les champs de recherche pour la recherche d'utilisateurs
    search_fields = ['email', 'first_name', 'last_name']

    # Définir les filtres pour filtrer les utilisateurs par rôle et statut du personnel
    list_filter = ['role', 'is_staff']

    # Définir les détails de l'utilisateur à afficher
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Informations supplémentaires', {'fields': ('role',)}),
    )

    # Définir les champs à afficher lors de la création d'un nouvel utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    # Définir le modèle utilisateur personnalisé
    model = User

# Enregistrer le modèle utilisateur personnalisé dans l'interface d'administration
admin.site.register(User, UserAdmin)
# # Supprimer le modèle utilisateur par défaut de l'interface d'administration
# admin.site.unregister(Group)

