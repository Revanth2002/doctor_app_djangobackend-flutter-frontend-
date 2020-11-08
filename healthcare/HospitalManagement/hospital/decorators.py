from django.contrib.auth.models import Group
from django.shortcuts import redirect,render

def doctoronly(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='Doctor':
            return view_func(request,*args,**kwargs)
        
        if group=='Patient':
            return redirect('patient')
    return wrapper_function

def patientonly(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name
        if group=='Patient':
            return view_func(request,*args,**kwargs)
        if group=='Doctor':
            return redirect('doctor')
    return wrapper_function
    