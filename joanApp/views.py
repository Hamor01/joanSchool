from django.shortcuts import render

from joanApp.models import Welcome, Student


# Create your views here.


def home(request):

    school = Welcome.objects.all()[:1]

    context = {'school':school}

    return render(request, 'index.html', context)





def course(request):
    return render(request, 'course.html')


def teachers(request):
    instance = Student.objects.all()[:1]
    context = {'instance':instance}
    return render(request, 'teachers.html', context)


def programs(request):
    return render(request, 'programs.html')

def contacts(request):
    return render(request, 'contacts.html')