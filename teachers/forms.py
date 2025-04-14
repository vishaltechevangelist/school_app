from django import forms

class TeachersForm(forms.Form):
    name = forms.CharField(min_length=5, label='Your Name', label_suffix='', error_messages={'required':'Your name field cannot be empty', 'min_length':'The name should be more than 5 characters'})
    email = forms.EmailField(required=False, label="Your Email", label_suffix='', help_text='We only accept email from gmail.com')
    phone_number = forms.IntegerField(label='Contact Number', label_suffix='')

