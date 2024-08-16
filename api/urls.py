from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('Produits', ProduitsViewSet)
router.register('Catégorie', CatégorieViewSet)
router.register('Pharmacie', PharmacieViewSet)
router.register(r'users', UserViewSet, basename='user')
router.register('Commande', CommandeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
   
]
