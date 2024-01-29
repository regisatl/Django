from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

# Create your views here.

def index(request):
      context = {
            "message": "Hello world !",
            "publication": datetime.datetime.now()
            }
      template = loader.get_template("mangalib/index.html")
      return HttpResponse(template.render(context, request))