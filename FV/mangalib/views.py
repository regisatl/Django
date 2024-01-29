from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import datetime

# Create your views here.

def index(request):
      context = {
            "message": "Bonjour et bienvenue sur ma bibliothèque de mangas et animés",
            "usersList": [
                  "admin",
                  "superviseur",
                  "teleconseiller",
                  "developper"
            ],
            "number": 1,
            "link": "http://mescrepes.fr/index.html?recette=sansoeufs&p=2"
            }
      template = loader.get_template("mangalib/index.html")
      return HttpResponse(template.render(context, request))