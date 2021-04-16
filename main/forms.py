from django import forms

class EntryForm(forms.Form):
    name = forms.CharField(max_length=255)
    url = forms.URLField(max_length=500,required=True)
    email = forms.EmailField(max_length=255,required=True)
    price = forms.DecimalField(max_digits=1000,decimal_places=2,required=True)