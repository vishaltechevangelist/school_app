from django import forms

class TeachersForm(forms.Form):
    name = forms.CharField()

