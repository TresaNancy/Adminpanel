from django.shortcuts import render
from django. http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm

# Create your views here.
def index(request):
    person = {
        'name': 'Nancy',
        'job': 'Python Developer',
        'place': 'Kochi'

    }
    return render(request, 'index.html',person)

def about(request):
    Numbers = {
        'num': 0
    }
    return render(request,'about.html',Numbers)

def booking(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'bookings.html',dict_form)
def doctors(request):
    dict_docs = {
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)
def contact(request):
    return render(request,'contact.html')
def department(request):

    dict_dept = {
        'dept': Departments.objects.all()
    }


    return render(request,'department.html',dict_dept)