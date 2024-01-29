from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def index(request):
      context = {
            "message": "Bienvenue sur le site de MangaLib",
            "username": "Régis ATTOLOU"
            }
      template = loader.get_template("mangalib/index.html")
      return HttpResponse(template.render(context, request))