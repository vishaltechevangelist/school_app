from django import forms
from students.models import Students
from django.core import validators

def start_s(value):
    if value[0] != 'S' and value[0] != 's':
        raise forms.ValidationError("Name should start with 'S'")

class StudentsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),
                           validators=[start_s, validators.MaxLengthValidator(10)],
                           label='Your Name')

    class Meta:
        model = Students
        # fields = ['name', 'email', 'phone_number', 'student_class', 'age', 'bio']
        fields = '__all__'  # 2nd approach if all model field need to be displayed on form
        # exclude = ['email'] # to exclude or not to display fields on form
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'student_class': 'Student Class',
            'age': 'Age',
            'bio': 'Your Details',
            'phone_number': 'Contact Number'
            }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'student_class':forms.NumberInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'bio':forms.Textarea(attrs={'class':'form-control'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control'}),
        }
        help_texts = {
            'email':'We only accept gmails'
        }
        error_messages = {
            'name' : {
                'required': 'Name field is required'
            },
            'email' : {
                'required': 'Email field is required'
            },  
        }
    
    # def clean(self):
    #     cleaned_data = super().clean()

    #     name = self.cleaned_data['name']
    #     email = self.cleaned_data['email']

    #     if name[0] != 'S' and name[0] != 's':
    #         raise forms.ValidationError("First letter of name should be 's'")
        
    #     if email[0] != 'S' and email[0] != 's':
    #         raise forms.ValidationError("First letter of email should be 's'")