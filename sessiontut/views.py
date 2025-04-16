from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    request.session['name'] = 'Vishal'
    request.session['fatherName'] = 'Dinesh'
    # request.session.set_expiry(5)
    return HttpResponse(f"Session set with expiry age {request.session.get_expiry_age()}")

def get(request):
    # return HttpResponse(f"{request.session['name']} father name is {request.session['fatherName']}")
    return HttpResponse(f"Father name is {request.session['fatherName']}")

def delete(request):
    # del request.session['name'] # partial deletion i.e row in django_session and sessionid cookie still exist hence flush method
    request.session.flush()
    request.session.clear_expired()
    return HttpResponse("Session deleted")

def update(request):
    request.session['fatherName'] = 'Vishal'
    return HttpResponse('Session data is updated')