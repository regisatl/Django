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
      name = models.CharField(max_length=60, unique=True)

class Book(models.Model):
      title = models.CharField(max_length=30, unique = True)
      quantity = models.IntegerField(default = 1)
      author = models.ForeignKey(Author, on_delete = models.DO_NOTHING)