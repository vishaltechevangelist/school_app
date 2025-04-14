from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from students.models import Students
from students.forms import StudentsForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/student/thank-you/')
    else:
        form = StudentsForm()
    return render(request, 'students/home.html', {'form':form})

def thank(request):
    return HttpResponse("Thank You, Data is saved")

def data(request):
    alldata = Students.objects.all()
    return render(request, 'students/alldata.html', {'alldata':alldata})

def update(request, id):
    student = Students.objects.get(id=id)
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            student.name = form.cleaned_data['name']
            student.email = form.cleaned_data['email']
            student.phone_number = form.cleaned_data['phone_number']
            student.bio = form.cleaned_data['bio']
            student.id = id
            student.save()
            return HttpResponseRedirect('/students/thank-you/')
    else:
        form = StudentsForm(initial={'name':student.name, 'email':student.email, 'phone_number':student.phone_number,
                                 'bio':student.bio, 'age':student.age, 'student_class':student.student_class})
    return render(request, 'students/update.html', {'form':form})

def delete(request, id):
    if request.method == 'POST':
        student = Students.objects.get(id=id)
        student.delete()
    return HttpResponseRedirect('/student/home/')