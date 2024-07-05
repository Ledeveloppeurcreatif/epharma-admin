from django import forms
from django.forms import ModelForm, Textarea
from.models import Catégorie,Produits,Pharmacie
from django.forms.fields import ImageField



class CatégorieForm(ModelForm):
    class Meta:
        model= Catégorie
        fields = "__all__"



class ProduitsForm(ModelForm):
    image = ImageField(
        required=False,
    )
    
    class Meta:
        model= Produits
        fields = "__all__"
        widgets = {
            "description": Textarea(attrs={"cols": 40, "rows": 5}),
        }
        help_texts = {
            "idProduit": ("Le champs ID doit etre unique."),
        }
        error_messages = {
            "nom": {
                "max_length": ("This writer's name is too long."),
            },
        }

class PharmacieForm(ModelForm):
     
     class Meta:
        model= Pharmacie
        fields = "__all__"
        

