from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author


"""
SELECT : all(), get()
WHERE : filter()
                  __gt, __lt, __gte, __lte, __startswith
ORDER BY : order_by()
LIMIT  : [:N]

INSERT : CREATE()

save(), delete()

Many-to-many : A*->B -> A*

One-to-one : 1 -> 1

raw()

"""
# Create your views here.

def index(request):
      context = {
            "books": Book.objects.all()
      }
      return render(request, "mangalib/index.html", context)


def show(request, book_id):
      context = {"book" : get_object_or_404(Book, pk =book_id)}
      return render (request, "mangalib/show.html", context)


def add(request):
      author = Author.objects.get(name="Masashi Kishimoto")
      book = Book.objects.create(title="Boruto Next Generation", quantity=10, author=author)
      return redirect('mangalib:index')

def edit(request):
      book = Book.objects.get(title="Dragon Ball")
      book.title = "Dragon Ball Super"
      book.save()
      return redirect("mangalib:index")
      
def remove(request):
      book = Book.objects.filter(title__startswith = "Dragon Ball")
      book.delete()
      return redirect("mangalib:index")

"""
many to many

book = Book.objects.get(pk = 1)
author = Author.objects.create(name = "Chuck Norris")
book.authors.add(author)

One to one

user.save()
user_identity.save()
"""
