"""
URL configuration for EpicEvents project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from epic.views import ClientViewSet, ContractViewSet ,EventViewSet


# Ici nous créons notre routeur
router = routers.SimpleRouter()
# Puis lui déclarons une url basée sur le mot clé ‘client’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/client/’
router.register('client', ClientViewSet, basename='client')
router.register('contract', ContractViewSet, basename='contract')
router.register('event', EventViewSet, basename='event')


from authentification.views import UserCreateAPIView

urlpatterns = [
    path('admin', admin.site.urls),
    path("api-auth/", include('rest_framework.urls')),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("signup/", UserCreateAPIView.as_view(), name="signup"),
    path('api/', include(router.urls))  # Il faut bien penser à ajouter les urls du router dans la liste des urls disponibles.
]
