from django.shortcuts import render
from .models import Produit

# Create your views here.
def index(request):
    produit_obj =Produit.objects.all()
    return render(request,'index.html',{'produit_obj':produit_obj})
