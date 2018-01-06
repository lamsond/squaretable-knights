from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from .models import Major
from .forms import EnrollmentForm

def index(request):
    context = {
            'options': ['Create New Application',
                'Check Status of Application',
                'Review Application (Admin)',],
            }
    return render(request, 'enroll/index.html', context)

def get_id(request):
    return HttpResponse("Enter student ID")

def apply(request):
    form = EnrollmentForm()
    return render(request, 'enroll/apply_form.html', {'form':form})

def check_status(request, student_id):
    return HttpResponse("Check status of application")

def review(request, student_id):
    return HttpResponse("Review application")


