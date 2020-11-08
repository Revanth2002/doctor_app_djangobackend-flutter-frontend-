from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
class Doctor(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name.username



class Patientdetails(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    age=models.TextField(null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    problem=models.TextField(null=True)
    medication=models.TextField(null=True)
    

    def get_absolute_url(self):
        return reverse('doctor')

    def __str__(self):
        return self.name.username




