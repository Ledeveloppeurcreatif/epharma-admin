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
        

class PharmacieSerializer(serializers.ModelSerializer):
   
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=1  
    )

    class Meta:
        model = Pharmacie
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
        extra_kwargs = {
            'produit': {'required': True},
        }
    def create(self, validated_data):
        # Journaliser les données validées
        print("Données validées :", validated_data)
        
        return super().create(validated_data)
