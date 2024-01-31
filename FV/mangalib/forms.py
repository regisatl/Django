from django import forms


"""
CharField
<input>
      type = "email"
"""

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