from django.urls import path

from . import views

app_name = 'joanApp'

urlpatterns = [
    path('', views.index, name='index.html'),
    path('course/', views.course, name='course.html'),
]