from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html', {'name_of_page': 'index'})


def course(request):
    return render(request, 'course.html', {'name_of_page':'course'})

