# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets,response,status, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from api.models import *
from backend.models import *
from api.serializers import *
from django.http import HttpResponse








class  ProduitsViewSet(viewsets.ModelViewSet):

    queryset = Produits.objects.all()
    serializer_class = ProduitsSerializer
    #permission_classes = [permissions.IsAdminUser]


class CatégorieViewSet(viewsets.ModelViewSet):

    queryset = Catégorie.objects.all()
    serializer_class = CatégorieSerializer
    #permission_classes = [permissions.IsAdminUser]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAdminUser]


class CommandeViewSet(viewsets.ModelViewSet):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    #permission_classes = [permissions.IsAdminUser]


@action(detail=False, methods=['post'])
def create_commande(self, request, *args, **kwargs):
    data = request.data

    # Print the received data
    print(f"Received data: {data}")

    # Extract product ID from the URL
    produit_url = data.get('produit')
    if produit_url:
        produit_id = produit_url.rstrip('/').split('/')[-1]
        # Print the extracted product ID
        print(f"Extracted product ID: {produit_id}")
        try:
            # Check if the product exists
            produit = Produits.objects.get(id=produit_id)
            data['produit'] = produit_id
        except Produits.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "Product URL is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Ensure required fields are present
    required_fields = ['quantite', 'username', 'useremail']
    for field in required_fields:
        if field not in data or not data[field]:
            return Response({"error": f"Missing required field: {field}"}, status=status.HTTP_400_BAD_REQUEST)

    # Create and validate the serializer
    serializer = self.get_serializer(data=data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Save the new Commande
    self.perform_create(serializer)
    headers = self.get_success_headers(serializer.data)

    # Return the response
    return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


# @api_view(['POST'])
# def accepter_commande(request, pk):
#     try:
#         commande = Commande.objects.get(pk=pk)
#         commande.status = 'Accepted'
#         commande.save()
        
#         # Copier la commande dans l'historique
#         Historique.objects.create(
#             date_commande=commande.date_commande,
#             quantite=commande.quantite,
#             username=commande.username,
#             useremail=commande.useremail,
#             produit=commande.produit,
#             status='Accepted'
#         )
        
#         # Supprimer la commande originale
#         #commande.delete()

#         return Response({'status': 'Commande acceptée'}, status=status.HTTP_200_OK)
#     except Commande.DoesNotExist:
#         return Response({'error': 'Commande non trouvée'}, status=status.HTTP_404_NOT_FOUND)
    


@api_view(['POST'])
def accepter_commande(request, pk):
    try:
        commande = Commande.objects.get(pk=pk)
        commande.status = 'Accepted'
        commande.save()
        
        # Copier la commande dans l'historique
        Historique.objects.create(
            date_commande=commande.date_commande,
            quantite=commande.quantite,
            username=commande.username,
            useremail=commande.useremail,
            produit=commande.produit,
            status='Accepted'
        )
        
        # Générer la facture
        invoice_buffer = generate_invoice(commande)
        
        # Créer la réponse HTTP avec le fichier PDF
        response = HttpResponse(invoice_buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="facture_{commande.pk}.pdf"'
        
        return response
        
    except Commande.DoesNotExist:
        return Response({'error': 'Commande non trouvée'}, status=status.HTTP_404_NOT_FOUND)








@api_view(['POST'])
def refuser_commande(request, pk):
    try:
        commande = Commande.objects.get(pk=pk)
        commande.status = 'Rejected'
        commande.save()
        
        # Copier la commande dans l'historique
        Historique.objects.create(
            date_commande=commande.date_commande,
            quantite=commande.quantite,
            username=commande.username,
            useremail=commande.useremail,
            produit=commande.produit,
            status='Rejected'
        )
        
        # Supprimer la commande originale
        #commande.delete()

        return Response({'status': 'Commande refusée'}, status=status.HTTP_200_OK)
    except Commande.DoesNotExist:
        return Response({'error': 'Commande non trouvée'}, status=status.HTTP_404_NOT_FOUND)



class PharmacieViewSet(viewsets.ModelViewSet):

    queryset = Pharmacie.objects.all()
    serializer_class = PharmacieSerializer
   # permission_classes = [permissions.IsAdminUser]



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'email' 
    #permission_classes = [permissions.IsAdminUser]
