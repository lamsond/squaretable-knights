from django.shortcuts import render
from django.http import HttpResponse

from .models import Student

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
    return HttpResponse("Create a new application")

def check_status(request, student_id):
    return HttpResponse("Check status of application")

def review(request, student_id):
    return HttpResponse("Review application")


