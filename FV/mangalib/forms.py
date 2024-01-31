from django import forms
from .models import Author, Book

"""
CharField
<input>
      type = "email"
"""
class BookForm(forms.ModelForm):
      author  = forms.ModelChoiceField(queryset=Author.objects.all(), label = "Auteur")
      
      class Meta:
            model = Book
            fields = ['title', 'author', 'quantity']
            labels = {'title': 'Titre', 'quantity': 'Quantité'}



# class SomeForm(forms.Form):
#       username = forms.CharField(label='Your username', max_length=30)
#       password = forms.CharField(label='Your password', widget=forms.PasswordInput)
#       bio = forms.CharField(label = "Biographie", widget = forms.Textarea)
      
#       languages = [('c', 'Langage C'), ('php', 'Langage PHP')]
#       language = forms.MultipleChoiceField(label="Langages connus", widget=forms.CheckboxSelectMultiple, choices=languages)

#       colors = [('1', "Rouge"), ('2', "Bleu"), ('3', "vert")]
#       color = forms.ChoiceField(label="Couleurdominante", choices=colors, widget=forms.RadioSelect)
      
#       countries = [('fr', "France"), ('jp', "Japon"), ('kr', "Corée du Sud")]
#       country = forms.ChoiceField(label="Country", choices=countries)