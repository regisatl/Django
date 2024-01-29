from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Book

# Create your views here.

def index(request):
      context = {"books": Book.objects.all()}
      return render(request, "mangalib/index.html", context)


def show(request, book_id):
      context = {"book" : get_object_or_404(Book, pk=book_id)}
      return render (request, "mangalib/show.html", context)