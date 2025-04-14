from django import forms
from django.core import validators


def start_s(value):
    if value[0] != 'S' and value[0] != 's':
        raise forms.ValidationError("Name should start with 'S'")

class TeachersForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                           min_length=5, label='Your Name', label_suffix='', 
                           error_messages={'required':'Your name field cannot be empty', 
                                           'min_length':'The name should be more than 5 characters'},
                                           validators=[start_s, validators.MaxLengthValidator(10)])
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control',
                                                            'placeholder':'Please enter your email'}), required=False, 
                                                            label="Your Email", label_suffix='', 
                                                            help_text='We only accept email from gmail.com',
                                                            validators=[start_s])
    phone_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label='Contact Number', label_suffix='')
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Bio', 'class':'form-control'}))

    # def clean(self):
    #     cleaned_data = super().clean()

    #     name = self.cleaned_data['name']
    #     email = self.cleaned_data['email']

    #     if name[0] != 'S' and name[0] != 's':
    #         raise forms.ValidationError("First letter of name should be 's'")
        
    #     if email[0] != 'S' and email[0] != 's':
    #         raise forms.ValidationError("First letter of email should be 's'")
        
