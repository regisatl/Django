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



class Author(models.Model):
      name = models.CharField(max_length=60, unique=True, verbose_name = "Nom")
      def __str__(self):
            return self.name
      class Meta:
            verbose_name = "Auteur"
            verbose_name_plural = "Auteurs"
      
class Book(models.Model):
      title = models.CharField(max_length=30, unique = True, verbose_name = "Titre")
      quantity = models.IntegerField(default = 1, verbose_name = "Quantité")
      author = models.ForeignKey(Author, on_delete = models.DO_NOTHING, verbose_name = "Auteur")
      
      def __str__(self):
            return self.title
      class Meta:
            verbose_name = "Livre"
            verbose_name_plural = "Livres"

