from django.urls import path

from . import views

app_name = 'joanApp'

urlpatterns = [
    path('', views.home, name='index.html'),
    path('course/', views.course, name='course.html'),
    path('teachers/', views.teachers, name='teachers.html'),
    path('programs/', views.programs, name='programs.html'),
    path('contacts/', views.contacts, name='contacts.html')
]