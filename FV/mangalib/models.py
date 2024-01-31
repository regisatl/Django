# Importation du module models du package django.db. 
# Ce module contient des classes qui aident à créer des modèles de base de données dans Django.
from django.db import models


# Create your models here.

"""
primary_key
unique
default
null
blank

CharField
IntegerField
DateField
DateTimeField
FloateField
EmailField
BooleanField

class Book(models.Model):
      authors = models.ManyToManyField(Author)

"""


# Définition de la classe Author qui hérite de models.Model
class Author(models.Model):
    # Définition d'un champ CharField pour le nom de l'auteur. Ce champ est unique et a une longueur maximale de 60 caractères.
    name = models.CharField(max_length=60, unique=True, verbose_name="Nom")

    # Méthode spéciale pour retourner une représentation sous forme de chaîne de caractères de l'objet Author.
    def __str__(self):
        return self.name

    # Classe Meta pour définir des options supplémentaires.
    class Meta:
        # Définition du nom verbeux pour un objet de cette classe.
        verbose_name = "Auteur"
        # Définition du nom verbeux au pluriel pour les objets de cette classe.
        verbose_name_plural = "Auteurs"


# Définition de la classe Book qui hérite de models.Model
class Book(models.Model):
    # Définition d'un champ CharField pour le titre du livre. Ce champ est unique et a une longueur maximale de 30 caractères.
    title = models.CharField(max_length=30, unique=True, verbose_name="Titre")
    # Définition d'un champ IntegerField pour la quantité de livres. Par défaut, la quantité est 1.
    quantity = models.IntegerField(default=1, verbose_name="Quantité")
    # Définition d'une relation ForeignKey avec la classe Author. Cela signifie qu'un livre a un auteur.
    author = models.ForeignKey(
        Author, on_delete=models.DO_NOTHING, verbose_name="Auteur"
    )

    # Méthode spéciale pour retourner une représentation sous forme de chaîne de caractères de l'objet Book.
    def __str__(self):
        return self.title

    # Classe Meta pour définir des options supplémentaires.
    class Meta:
        # Définition du nom verbeux pour un objet de cette classe.
        verbose_name = "Livre"
        # Définition du nom verbeux au pluriel pour les objets de cette classe.
        verbose_name_plural = "Livres"
