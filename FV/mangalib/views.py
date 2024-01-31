# Importation des modules nécessaires
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Author  # Importation des modèles Book et Author
from .forms import BookForm  # Importation du formulaire pour le modèle Book

# Les commentaires suivants expliquent comment utiliser l'ORM Django pour interagir avec la base de données
"""
SELECT : all(), get()  # Pour sélectionner tous les objets ou un objet spécifique
WHERE : filter()  # Pour filtrer les objets selon certains critères
                  __gt, __lt, __gte, __lte, __startswith  # Opérateurs pour les filtres
ORDER BY : order_by()  # Pour trier les objets
LIMIT  : [:N]  # Pour limiter le nombre d'objets retournés

INSERT : CREATE()  # Pour créer un nouvel objet

save(), delete()  # Pour sauvegarder un objet modifié ou supprimer un objet

Many-to-many : A*->B -> A*  # Relation many-to-many

One-to-one : 1 -> 1  # Relation one-to-one

raw()  # Pour exécuter une requête SQL brute
"""

# Définition des vues


def index(request):  # Vue pour la page d'accueil
    context = {"books": Book.objects.all()}  # Récupération de tous les livres
    return render(
        request, "mangalib/index.html", context
    )  # Rendu de la page avec le contexte


def show(request, book_id):  # Vue pour afficher un livre spécifique
    context = {
        "book": get_object_or_404(Book, pk=book_id)
    }  # Récupération du livre ou renvoie une erreur 404 si non trouvé
    return render(
        request, "mangalib/show.html", context
    )  # Rendu de la page avec le contexte


def add(request):  # Vue pour ajouter un nouveau livre
    if request.method == "POST":  # Si la requête est une requête POST
        form = BookForm(request.POST)  # Création du formulaire avec les données POST
        if form.is_valid():  # Si le formulaire est valide
            form.save()  # Sauvegarde du nouveau livre
            return redirect("mangalib:index")  # Redirection vers la page d'accueil
    else:
        form = (
            BookForm()
        )  # Si la requête n'est pas une requête POST, création d'un formulaire vide
    return render(
        request, "mangalib/book-form.html", {"form": form}
    )  # Rendu de la page avec le formulaire


def edit(request, book_id):  # Vue pour modifier un livre existant
    book = get_object_or_404(
        Book, pk=book_id
    )  # Récupération du livre ou renvoie une erreur 404 si non trouvé

    if request.method == "POST":  # Si la requête est une requête POST
        form = BookForm(
            request.POST, instance=book
        )  # Création du formulaire avec les données POST et l'instance du livre
        if form.is_valid():  # Si le formulaire est valide
            form.save()  # Sauvegarde des modifications du livre
            return redirect("mangalib:index")  # Redirection vers la page d'accueil
    else:
        form = BookForm(
            instance=book
        )  # Si la requête n'est pas une requête POST, création du formulaire avec l'instance du livre
    return render(
        request, "mangalib/book-form.html", {"form": form}
    )  # Rendu de la page avec le formulaire


def remove(request, book_id):  # Vue pour supprimer un livre
    book = Book.objects.get(pk=book_id)  # Récupération du livre
    book.delete()  # Suppression du livre
    return redirect("mangalib:index")  # Redirection vers la page d'accueil


# Les commentaires suivants expliquent comment gérer les relations many-to-many et one-to-one
"""
many to many

book = Book.objects.get(pk = 1)  # Récupération d'un livre
author = Author.objects.create(name = "Chuck Norris")  # Création d'un nouvel auteur
book.authors.add(author)  # Ajout de l'auteur au livre

One to one

user.save()  # Sauvegarde d'un utilisateur
user_identity.save()  # Sauvegarde de l'identité de l'utilisateur
"""
