from django import forms


"""
CharField
"""

class SomeForm(forms.Form):
      username = forms.CharField(label='Your username', max_length=60)