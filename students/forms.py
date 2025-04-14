from django import forms
from students.models import Students

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'email', 'phone_number', 'student_class', 'age', 'bio']