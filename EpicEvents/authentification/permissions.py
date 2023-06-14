from rest_framework.permissions import BasePermission
from authentification.models import User


class IsSuperOrGestion(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # user = User.objects.filter(email=request.user.email).first()

            if request.user.is_superuser or request.user.role == "GESTION":
                return True

        return False
