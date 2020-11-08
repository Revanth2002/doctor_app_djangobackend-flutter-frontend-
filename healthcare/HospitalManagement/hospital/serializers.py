from rest_framework import serializers
from .models import Patientdetails

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patientdetails
        fields='__all__'