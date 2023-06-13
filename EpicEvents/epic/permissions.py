from rest_framework.permissions import BasePermission

class SalesOrGestion(BasePermission):

    """ La permission pour la vie CLient qui permet de voir ou modifier un client,
     seulement si le user à le role VENTES et que le client est lié au user"""
    # def has_permission(self, request, view):
    #     if request.user.role == "VENTE":
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == "VENTE" and view.action != "destroy" :
            return obj.contact_ventes == request.user
        elif request.user.role == "GESTION" :
            return True
        return False


class SupportOrSalesOrGestion(BasePermission):

    """ La permission pour la vie CLient qui permet de voir ou modifier un client,
     seulement si le user à le role Support et que le client est lié au user"""

    def has_object_permission(self, request, view, obj):
        if request.user.role in ["VENTE","SUPPORT"] and view.action != "destroy" :
            return obj.support_contact == request.user or obj.contract.contact_ventes == request.user
        elif request.user.role == "GESTION" :
            return True
        return False

class CanViewAssignedEventClients(BasePermission):
    """ la permission d'affichage les clients d'un event,
    seulement si le user à le role SUPPORT et que l'event est lié au user"""

    def has_object_permission(self, request, view, obj):
        if request.user.role == "SUPPORT":
            # Vérifier si l'utilisateur a le rôle "SUPPORT" et si l'événement lui est attribué
            if obj.support_contact == request.user:
                return True
        return False