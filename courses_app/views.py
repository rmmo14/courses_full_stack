from django.shortcuts import render, redirect
from .models import theCourse
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        'allCourses': theCourse.objects.all()
    }
    return render(request, "index.html", context)

def add(request):
    errors = theCourse.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    theCourse.objects.create(
        name = request.POST['name'],
        description = request.POST['description']
    )
    return redirect('/')

def remove(request, current_id):
    this_course = theCourse.objects.get(id=current_id)
    context = {
        'courses': this_course
    }
    return render(request, "destroy.html", context)

def delete(request, current_id):
    this_course = theCourse.objects.get(id=current_id)
    this_course.delete()
    return redirect ('/')

# def allcourses(request):
