# Importation du module forms du package django. Ce module contient des classes qui aident à créer des formulaires dans Django.
from django import forms

# Importation des classes Author et Book du module models du package courant.
from .models import Author, Book


# Définition de la classe BookForm qui hérite de forms.ModelForm. Cette classe représente un formulaire pour créer ou modifier un objet Book.
class BookForm(forms.ModelForm):
    # Définition d'un champ ModelChoiceField pour l'auteur du livre. Ce champ représente une liste déroulante des auteurs existants.
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Auteur")

    # Classe Meta pour définir des options supplémentaires.
    class Meta:
        # Spécification du modèle à utiliser, ici c'est le modèle Book.
        model = Book
        # Spécification des champs du modèle à inclure dans le formulaire.
        fields = ["title", "author", "quantity"]
        # Spécification des labels à utiliser pour les champs du formulaire.
        labels = {"title": "Titre", "quantity": "Quantité"}


# Définition de la classe SomeForm qui hérite de forms.Form. Cette classe représente un formulaire personnalisé.
# class SomeForm(forms.Form):
#     # Définition d'un champ CharField pour le nom d'utilisateur. Ce champ a une longueur maximale de 30 caractères.
#     username = forms.CharField(label="Your username", max_length=30)
#     # Définition d'un champ CharField pour le mot de passe. Ce champ utilise un widget PasswordInput pour masquer la saisie.
#     password = forms.CharField(label="Your password", widget=forms.PasswordInput)
#     # Définition d'un champ CharField pour la biographie. Ce champ utilise un widget Textarea pour permettre la saisie de texte multiligne.
#     bio = forms.CharField(label="Biographie", widget=forms.Textarea)

#     # Définition d'une liste de langages.
#     languages = [("c", "Langage C"), ("php", "Langage PHP")]
#     # Définition d'un champ MultipleChoiceField pour les langages connus. Ce champ représente une liste de cases à cocher.
#     language = forms.MultipleChoiceField(
#         label="Langages connus", widget=forms.CheckboxSelectMultiple, choices=languages
#     )

#     # Définition d'une liste de couleurs.
#     colors = [("1", "Rouge"), ("2", "Bleu"), ("3", "vert")]
#     # Définition d'un champ ChoiceField pour la couleur dominante. Ce champ représente une liste de boutons radio.
#     color = forms.ChoiceField(
#         label="Couleurdominante", choices=colors, widget=forms.RadioSelect
#     )

#     # Définition d'une liste de pays.
#     countries = [("fr", "France"), ("jp", "Japon"), ("kr", "Corée du Sud")]
#     # Définition d'un champ ChoiceField pour le pays. Ce champ représente une liste déroulante.
#     country = forms.ChoiceField(label="Country", choices=countries)
