# listings/forms.py

from django import forms
from listings.models import Band, Comic



class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        exclude = ('hero',) 


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        exclude = ('active', 'official_homepage')  

