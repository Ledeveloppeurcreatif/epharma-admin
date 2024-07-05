from rest_framework import serializers
from api.models import *
#from api.serializers import UserSerializer

class ProduitsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produits
        fields = '__all__'


class CatégorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catégorie
        fields = '__all__'
        


class PharmacieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pharmacie
        fields = '__all__'



class CommandeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail', source='pharmacie',)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'url')