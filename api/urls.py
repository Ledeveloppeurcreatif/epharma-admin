from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('Produits', ProduitsViewSet)
router.register('Catégorie', CatégorieViewSet)
router.register('Pharmacie', PharmacieViewSet)
router.register('Commande', CommandeViewSet)
router.register('User', UserViewSet ,basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
   
]
