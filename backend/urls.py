from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('page/', views.saveCatégorie, name='saveCatégorie'),
     path('view/', views.view, name='view'),
     path('ajouter_produit/', views.ajouter_produit, name='ajouter_produit'),
     path('liste_produits/', views.liste_produits, name='liste_produits'),
     path('ajouter_pharmacie/', views.ajouter_pharmacie, name='ajouter_pharmacie'),
     path('liste_pharmacie/', views.liste_pharmacie, name='liste_pharmacie'),
     path('modifypharmacie/<int:id>/', views.modifypharmacie, name='modifypharmacie'),
     path('deletepharmacie/<int:id>/', views.deletepharmacie, name='deletepharmacie'),
     path('modifyProduit/<int:id>/', views.modifyProduit, name='modifyProduit'),
     path('deleteProduit/<int:id>/', views.deleteProduit, name='deleteProduit'),
     path('recherche_produit/', views.recherche_produit, name='recherche_produit'),
     path('modifier/<int:id>/', views.ModifyCategorie, name='ModifyCategorie'),
     path('deleteCategorie/<int:id>/', views.deleteCategorie, name='deleteCategorie'),
     path('Logo/', views.Logo, name='Logo'),
     path('Dashboard/', views.Dashboard, name='Dashboard'),
     # path('profile/', views.profile, name='profile'),



     #urls authentification
    #path('', views.dashboard, name='dashboard'),
    path('', views.connexion, name='connexion'),
    path('inscription', views.inscription, name='inscription'),
    path('sortie', views.sortie, name='sortie'),
    path('password_oublier', views.password_oublier, name='password_oublier'),
    path('modifier_password', views.modifier_password, name='modifier_password'),
     
    
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
