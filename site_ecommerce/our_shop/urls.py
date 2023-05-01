from django.urls import path
from .views import index, information


urlpatterns = [
    path('', index, name='home'),
    #url dynamique depen de id
    path('<int:idprod>',information, name='information' ),
]