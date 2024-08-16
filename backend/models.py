from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Pharmacie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pharmacie',default=1)
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='pharmacies/photos/', blank=True, null=True)
    nom = models.CharField(blank=True, null=True)
    adresse = models.CharField(max_length=255,blank=True, null=True)  
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=255)
    repassword = models.CharField(max_length=255)
    proprietaire = models.CharField(max_length=255,blank=True, null=True)
    numero_ordre = models.CharField(max_length=100,blank=True, null=True)
    licence_exploitation = models.FileField(upload_to='pharmacie/autorisation/', blank=True, null=True)
    attestation_professionnelle = models.FileField(upload_to='pharmacie/attestation/', blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    

    def __str__(self):
        return self.nom
    




class inscription(models.Model):
    id = models.AutoField(primary_key=True)
    photo = models.ImageField(upload_to='pharmacies/photos/', blank=True, null=True)
    nom = models.CharField(blank=True, null=True)
    adresse = models.CharField(max_length=255,blank=True, null=True)  
    email = models.EmailField(blank=True, null=True)
    proprietaire = models.CharField(max_length=255,blank=True, null=True)
    numero_ordre = models.CharField(max_length=100,blank=True, null=True)
    licence_exploitation = models.FileField(upload_to='pharmacie/autorisation/', blank=True, null=True)
    attestation_professionnelle = models.FileField(upload_to='pharmacie/attestation/', blank=True, null=True)
    
    

class Catégorie(models.Model):
    idCategorie = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Produits(models.Model):
    idProduit = models.AutoField(primary_key=True)
    image = models.ImageField(null=False, upload_to='Produits',)
    Medicament = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    categorie = models.ForeignKey(Catégorie, on_delete=models.CASCADE)
    auteur = models.ForeignKey(Pharmacie, on_delete=models.CASCADE, related_name='pharmacie',default=1)
 
    def __str__(self):
        return self.Medicament
        


class Commande(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    id= models.AutoField(primary_key=True)
    date_commande = models.DateTimeField(default=timezone.now)
    quantite = models.PositiveIntegerField()
    username = models.CharField(max_length=255, default='default_username')
    useremail = models.EmailField(max_length=255,default='default@example.com') 
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending') 


    def __str__(self):
        return self.id
    

class Historique(models.Model):
     date_commande = models.DateTimeField(default=timezone.now)
     quantite = models.IntegerField()
     username =  models.CharField(max_length=255, default='default_username')
     useremail = models.EmailField(max_length=255,default='default@example.com') 
     produit = models.ForeignKey(Produits, on_delete=models.CASCADE)
     status = models.CharField(max_length=10, choices=Commande.STATUS_CHOICES)



class Vente(models.Model):
    id = models.AutoField(primary_key=True)
    produit = models.ForeignKey(Produits, on_delete=models.CASCADE,default=1)
    quantite = models.IntegerField()
    client = models.CharField(max_length=255)
    date_commande = models.DateTimeField(default=timezone.now)



class Facture(models.Model):
    vente = models.OneToOneField(Vente, on_delete=models.CASCADE)
    date_facture = models.DateTimeField(default=timezone.now)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'Facture {self.id} pour Vente {self.vente.id}'



















    #horaires_ouverture = models.TextField()
    #telephone = models.CharField(max_length=20)
    # attestation_professionnelle = models.FileField(upload_to='pharmacie/attestation/', blank=True, null=True)
    # autorisation_creation = models.FileField(upload_to='pharmacie/autorisation/', blank=True, null=True)
    # certificat_conformite = models.FileField(upload_to='pharmacie/autorisation/', blank=True, null=True)   
    # proprietaire_diplome = models.FileField(upload_to='pharmacie/diplome/', blank=True, null=True)
    # assurance_responsabilite = models.FileField(upload_to='pharmacie/assurance/', blank=True, null=True)
    # details_assurance = models.TextField(blank=True, null=True)
    # tmoney_number = models.CharField(max_length=20, blank=True, null=True)
    # flooz_number = models.CharField(max_length=20, blank=True, null=True)
    # declaration_conformite_donnees = models.FileField(upload_to='pharmacie/protection/', blank=True, null=True)
    # politique_confidentialite = models.FileField(upload_to='pharmacie/politique/', blank=True, null=True)
    # services_offerts = models.TextField(blank=True, null=True)
    # procedure_gestion_reclamations = models.TextField(blank=True, null=True) 
    # numero_identification_fiscale = models.CharField(max_length=100, blank=True, null=True)
    # autorisation_vente_en_ligne = models.FileField(upload_to='pharmacie/autorisation/', blank=True, null=True)
    # plan_locaux = models.FileField(upload_to='pharmacie/autorisation/', blank=True, null=True)







# class Commande(models.Model):
#     id_commande = models.AutoField(primary_key=True)
#     dateCommande = models.DateTimeField()
#     client = models.ForeignKey(Clients, on_delete=models.CASCADE)
#     panier = models.OneToOneField(Panier, on_delete=models.CASCADE)
    


# class Clients(models.Model):
#     idClients = models.AutoField(primary_key=True)
#     nom = models.CharField(max_length=255)
#     prenom = models.CharField(max_length=255)
#     adresseMail = models.EmailField(max_length=255)
#     mot_de_passe = models.CharField(max_length=255)


# class Messages(models.Model):
#     informations = models.TextField()
#     idClient = models.ForeignKey(Clients, on_delete=models.CASCADE)
    

# class Pharmaciens(models.Model):
#     nom = models.CharField(max_length=255)
#     coordonnees = models.CharField(max_length=255)
#     pharmacie = models.ForeignKey(Pharmacie, on_delete=models.CASCADE)



   
