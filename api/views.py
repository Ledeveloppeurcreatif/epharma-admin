# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets,response,status
from api.models import *
from api.serializers import *

class  ProduitsViewSet(viewsets.ModelViewSet):

    queryset = Produits.objects.all()
    serializer_class = ProduitsSerializer
    


class CatégorieViewSet(viewsets.ModelViewSet):

    queryset = Catégorie.objects.all()
    serializer_class = CatégorieSerializer




class CommandeViewSet(viewsets.ModelViewSet):

    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer







class PharmacieViewSet(viewsets.ModelViewSet):

    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer



class UserViewSet(viewsets.ModelViewSet):

    queryset =User.objects.all()
    serializer_class = UserSerializer
