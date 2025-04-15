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
    # raise Exception("Get data raising exception!!!")
    alldata = Students.objects.all()
    # return render(request, 'students/alldata.html', {'alldata':alldata})
    response = render(request, 'students/alldata.html', {'alldata':alldata})
    response.set_cookie('name', 'Adharv', httponly=True)
    return response

def update(request, id):
    student = Students.objects.get(id=id)
    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            return HttpResponseRedirect('/student/all-data/')
    else:
        form = StudentsForm(instance=student)
    return render(request, 'students/update.html', {'form':form})

def delete(request, id):
    if request.method == 'POST':
        student = Students.objects.get(id=id)
        student.delete()
    return HttpResponseRedirect('/student/home/')

def setCookie(request):
    response = HttpResponse('Set')
    response.set_cookie('theme', 'dark', max_age=5)
    response.set_cookie('name','vishal')
    return response

def getCookie(request):
    return HttpResponse(f"<h1>GET</h1> {request.COOKIES}")

def deleteCookie(request):
    response = HttpResponse('Deleted')
    response.delete_cookie('name')
    return response

def updateCookie(request):
    response = HttpResponse('Updated')
    response.set_cookie('name', 'Priyanka')
    return response