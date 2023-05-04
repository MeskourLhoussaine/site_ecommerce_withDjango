from django.shortcuts import render
from .models import Produit
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    produit_obj =Produit.objects.all()
    item_name = request.GET.get('item-name')
    if item_name != '' and item_name is not None:
        produit_obj = Produit.objects.filter(nom__icontains=item_name)
    paginator = Paginator(produit_obj, 4)
    page = request.GET.get('page')
    produit_obj = paginator.get_page(page)
    return render(request,'index.html',{'produit_obj':produit_obj})
def information(request, idprod):
    produit_obj = Produit.objects.get(id=idprod)
    return render(request,'information.html',{'produit_obj':produit_obj})
def checkout(request):
    return render(request,'checkout.html')
