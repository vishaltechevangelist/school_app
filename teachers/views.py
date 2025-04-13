from django.shortcuts import render
from teachers.forms import TeachersForm

# Create your views here.
def home(request):
    form = TeachersForm()
    return render(request, 'teachers/home.html', {'form':form})