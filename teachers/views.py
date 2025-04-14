from django.shortcuts import render
from teachers.forms import TeachersForm
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():
            # logic to save data in db
            return HttpResponseRedirect('/teacher/thank-you/')
    else:
        form = TeachersForm()
        return render(request, 'teachers/home.html', {'form':form})

def thank(request):
    return HttpResponse("Thank You, Data is saved")