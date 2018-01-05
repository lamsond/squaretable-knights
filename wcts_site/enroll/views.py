from django.shortcuts import render
from django.http import HttpResponse

from .models import Student
from .models import Major

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
    #major_list = Major.objects
    context = {}#{'major_list': major_list,}
    return render(request, 'enroll/apply_static.html', context)

def check_status(request, student_id):
    return HttpResponse("Check status of application")

def review(request, student_id):
    return HttpResponse("Review application")


