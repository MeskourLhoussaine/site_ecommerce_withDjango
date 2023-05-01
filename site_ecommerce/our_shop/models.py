from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=150)
    date_aj = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_aj']

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=150)
    prx = models.FloatField()
    description = models.TextField()
    categorie = ForeignKey(Categorie,related_name='categorie', on_delete = models.CASCADE)
    image = models.CharField(max_length=4000)
    date_aj = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_aj']


    def __str__(self):
        return self.nom