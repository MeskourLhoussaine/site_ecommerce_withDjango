from django.contrib import admin
from .models import Categorie,Produit,Commande
# Register your models here.
class AdminCategorie(admin.ModelAdmin):
    list_display =('nom','date_aj')

class AdminProduit(admin.ModelAdmin):
    list_display = ('nom','prx','categorie','date_aj')
admin.site.register(Produit,AdminProduit)
admin.site.register(Categorie,AdminCategorie)
admin.site.register(Commande)