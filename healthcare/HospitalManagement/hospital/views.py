from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import Register
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .decorators import doctoronly,patientonly
from django.contrib.auth.models import User
from .models import Patientdetails,Doctor
from django.views.generic import UpdateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import PatientSerializer

class PatientApi(generics.RetrieveUpdateAPIView):
    queryset=Patientdetails.objects.all()
    serializer_class = PatientSerializer
   

def home(request):
    return render(request,'home.html')

def register_user(request):
    r=Register()
    if request.method=='POST':
        r=Register(request.POST)
        if r.is_valid():
            user=r.save()
            username=r.cleaned_data.get('username')
            group=Group.objects.get(name='Patient')
            print(type(group))
            user.groups.add(group)
            print(user.groups)
            print(type(user.groups))
            if user.groups==group:
                print('YES')
            else:
                print('NO')
            return HttpResponse('You are added to the group:')
    return render(request,'home.html',{'form':r})

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('doctor')
    return render(request,'login.html')

@login_required(login_url='login')
@doctoronly
def doctor(request):
    doctor_name=User.objects.get(username=request.user)
    doctor_object=Doctor.objects.get(name=doctor_name)
    patients=doctor_object.patientdetails_set.all()

    return render(request,'doctorpage.html',context={'p':patients})

@login_required(login_url='login')
@patientonly
def patient(request):
    p=Patientdetails.objects.get(name=request.user)
    return render(request,'patientpage.html',{"p":p})


def logou_user(request):
    logout(request)
    return redirect('/')

@login_required
def createpatient(request):
    create=Register()
    if request.method=='POST':
        create=Register(request.POST)
        if create.is_valid():
            usersw=create.save()
            username=create.cleaned_data.get('username')
            group=Group.objects.get(name='Patient')
            usersw.groups.add(group)
            name=User.objects.get(username=username)
            doctor=Doctor.objects.get(name=request.user)
            p=Patientdetails(name=name,doctor=doctor)
            p.save()
            return redirect('doctor')
    return render(request,'createpatient.html',{'f':create})
        
def addpatienttodoctor(request,patient):
    name=User.objects.get(username=patient)
    doctor=Doctor.objects.get(name=request.user)
    p=Patientdetails(name=name,doctor=doctor)
    p.save()
    return redirect('doctor')


class patientupdateview(UpdateView):
    fields=('age','problem','medication')
    model=Patientdetails
    template_name='patientdetails_form.html'


def detailviewdoctor(request,pk):
    pat=Patientdetails.objects.get(id=pk)
    p=User.objects.get(username=pat.name)

    return render(request,'detailview.html',{'pat':pat,'p':p})
@api_view(['GET'])


def patientlist(request):
    patients=Patientdetails.objects.all()
    serializer=PatientSerializer(patients,many=True)
    for i in serializer.data:
        x=i['name']
        g=i['doctor']
        n=User.objects.get(id=x)
        i['name']=n.username
        d=Doctor.objects.get(id=g)
        i['doctor']=d.name.username
    return Response(serializer.data)
