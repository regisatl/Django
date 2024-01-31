from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Author
from .forms import BookForm

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

  # context = {
      #       "books": Book.objects.all()
      # }
      # return render(request, "mangalib/index.html", context)

"""
# Create your views here.

def index(request):
      context = { "books": Book.objects.all() }
      return render(request, "mangalib/index.html", context)
      

def show(request, book_id):
      context = {"book" : get_object_or_404(Book, pk =book_id)}
      return render (request, "mangalib/show.html", context)


def add(request):
      if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                  form.save()
                  return redirect("mangalib:index")
      else:
            form = BookForm()
      return render(request, "mangalib/book-form.html", {"form" : form})

def edit(request, book_id):
      book = get_object_or_404(Book, pk = book_id)
      
      if request.method == 'POST':
            form = BookForm(request.POST, instance = book)
            if form.is_valid():
                  form.save()
                  return redirect("mangalib:index")
      else:
            form = BookForm(instance = book)
      return render(request, "mangalib/book-form.html", {"form" : form})
      
def remove(request, book_id):
      book = Book.objects.get(pk = book_id)
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
