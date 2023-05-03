from django.urls import path
from .views import index, information,checkout



urlpatterns = [
    path('', index, name='home'),
    path('<int:idprod>',information, name='information'),
    path('checkout',checkout, name='checkout'),

]