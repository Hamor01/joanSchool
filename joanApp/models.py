from django.db import models

# Create your models here.


class Welcome(models.Model):
    TopMessage = models.CharField(max_length=50)
    paragraph = models.CharField(max_length=100)


    def __str__(self):
        return self.TopMessage


class Student(models.Model):
    h1 = models.CharField(max_length=50)
    para1 = models.CharField(max_length=200)
    h3 = models.CharField(max_length=50)
    para2 = models.CharField(max_length=250)
    para3 = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.h1

