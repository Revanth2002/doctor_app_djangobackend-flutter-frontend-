"""HospitalManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from hospital.views import register_user,login_user,doctor,patient,logou_user,createpatient,patientupdateview,detailviewdoctor,patientlist,PatientApi
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register_user,name='register'),
    path('',login_user,name='login'),
    path('doctor/',doctor,name='doctor'),
    path('patient/',patient,name='patient'),
    path('logout/',logou_user,name='logout'),
    path('create/',createpatient,name='createpatient'),
    path('update/<int:pk>',patientupdateview.as_view(),name='update'),
    path('detail/<int:pk>',detailviewdoctor,name='detail'),
    path('list/',patientlist,name='list'),
    path("<int:pk>",PatientApi.as_view())
   # path(" ",PatientListAPi.as_view())
]
