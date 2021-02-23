from django.db import models


# Create your models here.

class Students(models.Model):
    student_email = models.EmailField(max_length=100)
    student_first_name = models.CharField(max_length=25)
    student_last_name = models.CharField(max_length=50)
    student_password = models.CharField(max_length=500)
    last_login = models.DateTimeField(auto_now=True)