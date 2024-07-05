from django.shortcuts import redirect, render
from backend.models import Catégorie,Produits,Pharmacie,Commande
from .forms import *
from django.core.mail import EmailMessage
from django.db.models import Q
from .models import Pharmacie
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.utils import timezone



@login_required
def  Logo(request):
    # pharmacie_account = request.user
    # pharmacie = Pharmacie.objects.filter(user=pharmacie_account)[0]
    return render (request,'logo.html')


@login_required
def  Dashboard(request):
 commandes = Commande.objects.all()
 return render (request,'dashboard.html',{'commandes': commandes})




# def profile(request, id):
#      if id:
#          user = get_object_or_404(Pharmacie, id=id)
#      else:
#       user = request.user
#      context = {
#          'name': id.name,
#          'adresse': id.adresse,
#          'telephone': id.telephone,
#          'email': id.email,
#     }
#      return render(request, 'profile.html', context)

@login_required
def saveCatégorie(request):
    if request.method =='POST':
        form = CatégorieForm(request.POST)

        cat1 = form.save()

        return redirect('view')
    
    else :
        form = CatégorieForm()

    return render (request, 'page.html',{'form':form}) 


def view(request):
    categories = Catégorie.objects.all()
    return render(request, 'view.html', {'categories': categories})


@login_required
def ModifyCategorie(request,id):
     #récuperation des données de la base de donnée
    category = Catégorie.objects.get(idCategorie=id)
    form = CatégorieForm(instance=category)
    if request.method =='POST': 
        form = CatégorieForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            # Rediriger vers une page de succès ou de liste des catégories

        return redirect('view')
        
    return render (request, 'page.html',{'form':form, 'Categorie':Catégorie}) 


@login_required
def deleteCategorie(request,id):
     #récuperation des données de la base de donnée
    category = Catégorie.objects.get(idCategorie=id)
    category.delete()
    return redirect('view')
        


@login_required
def ajouter_produit(request):
    print("hello")
    if request.method =='POST':
        form = ProduitsForm(request.POST,request.FILES)
        
        if form.is_valid():
            img = form.cleaned_data.get("image")
            form.save()
            return redirect('liste_produits')
    
    else :
        form = ProduitsForm()

    return render (request, 'formulaire_produit.html',{'form':form}) 


def liste_produits(request):
    produit = Produits.objects.all()
    return render(request, 'affichage.html', {'produits': produit})





@login_required  
def modifyProduit(request,id):
     #récuperation des données de la base de donnée
    product = Produits.objects.get(idProduit=id)
  
   
    if request.method =='POST': 
        form = ProduitsForm(request.POST, instance=product)
        if form.is_valid():
            product =  form.save()
          
        

        return redirect('liste_produits')
    
    else :
        print("let's modify")
        form = ProduitsForm(instance=product)
        print(form)
    return render (request, 'formulaire_produit.html',{'form':form, 'produits': product}) 


@login_required
def deleteProduit(request,id):
     #récuperation des données de la base de donnée
    product = Produits.objects.get(idProduit=id)
    product.delete()
    return redirect('liste_produits')
        



@login_required
@permission_required('ajouter_pharmacie', raise_exception=True)
def ajouter_pharmacie(request):
    print("hello")
    if request.method =='POST':
        form = PharmacieForm(request.POST,request.FILES)
        
        if form.is_valid():
            img = form.cleaned_data.get("image")
            form.save()
            return redirect('liste_pharmacie')
    
    else :
        form = PharmacieForm()

    return render (request, 'formulaire_Pharmacie.html',{'form':form}) 

@login_required
@permission_required('liste_pharmacie', raise_exception=True)
def liste_pharmacie(request):
    pharmacie = Pharmacie.objects.all()
    return render(request, 'pharmacie.html', {'pharmacies': pharmacie})


@login_required
@permission_required('modifypharmacie', raise_exception=True)
def modifypharmacie(request,id):
     #récuperation des données de la base de donnée
    pharmacy = Pharmacie.objects.get(id=id)

    if request.method =='POST': 
        form = PharmacieForm(request.POST, instance=pharmacy)
        if form.is_valid():
            pharmacy =  form.save()
        return redirect('liste_pharmacie')
    
    else :
        print("let's modify")
        form = PharmacieForm(instance=pharmacy)
        print(form)
    return render (request, 'formulaire_Pharmacie.html',{'form':form, 'pharmacies': pharmacy}) 


 


@login_required
@permission_required('deletepharmacie', raise_exception=True)
def deletepharmacie(request,id):
     #récuperation des données de la base de donnée
    pharmacy = Pharmacie.objects.get(id=id)
    pharmacy .delete()
    return redirect('liste_pharmacie')





@login_required
def recherche_produit(request):
    if request.method == 'POST':
        recherche = request.POST.get('recherche')
        produits = Produits.objects.filter(Medicament__icontains=recherche)
        categories = Catégorie.objects.filter(nom__icontains=recherche)
        return render(request, 'resultats_recherche.html', {'produits': produits, 'categories': categories})
    else:
        return render(request, 'formulaire_recherche.html')








#views authentification

def connexion(request):
      if request.method == "POST":
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        user = User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username, password=password)
            

            if auth_user:
                login(request, auth_user)
                return redirect('Logo')
            else:
                print("mot de pass incorrecte")
        else:
            print("User does not exist")

      return render(request, 'login.html', {})
   



def inscription(request):
    error = False
    message = ""

    if request.method == "POST":
        photo = request.FILES.get('photo')
        nom = request.POST.get('nom')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        proprietaire = request.POST.get('proprietaire')
        numero_ordre = request.POST.get('numero_ordre')
        licence_exploitation = request.FILES.get('licence_exploitation')
        attestation_professionnelle = request.FILES.get('attestation_professionnelle')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        try:
            validate_email(email)
        except:
            error = True
            message = "Entrez un email valide svp!"

        if not error:
            if password != repassword:
                error = True
                message = "Les deux mots de passe ne correspondent pas!"

        if not error:
            user = User.objects.filter(email=email).first()
            if user:
                error = True
                message = f"Un utilisateur avec cet email {email} existe déjà!"

        if not error:
            print(nom)
            print(password)
            print(email)
            user = User.objects.create_user(
                email=email,
                password=password,
                username=nom,
                last_login=timezone.now()
            )
            user.save()
            print(user.id)
            pharmacie = Pharmacie.objects.create(
                nom=nom,
                adresse=adresse,
                email=email,
                password=password,
                proprietaire=proprietaire,
                numero_ordre=numero_ordre,
                photo=photo,
                licence_exploitation=licence_exploitation,
                attestation_professionnelle=attestation_professionnelle,
                user = user
            )
            print(pharmacie.photo)
            pharmacie.save()
           

            return redirect('connexion')

        context = {
            'error': error,
            'message': message
        }

        return render(request, 'register.html', context)

    return render(request, 'register.html', {})
    




#def dashboard(request):
    return render(request, 'admin.html', {})

def sortie(request):
    logout(request)
    return redirect('connexion')


def password_oublier(request):
    error = False
    success = False
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            print("processing forgot password")
            html = """
                <p> Hello, merci de cliquer pour modifier votre email </p>
            """

            msg = EmailMessage(
                "Modification de mot de pass!",
                html,
                "soroib0879@gmail.com",
                ["soro4827@gmail.com"],
            )

            msg.content_subtype = 'html'
            msg.send()
            
            message = "processing forgot password"
            success = True
        else:
            print("user does not exist")
            error = True
            message = "user does not exist"
    
    context = {
        'success': success,
        'error':error,
        'message':message
    }
    return render(request, "forgot_password.html", context)
    


def modifier_password(request):
    return render(request, "update_password.html", {})