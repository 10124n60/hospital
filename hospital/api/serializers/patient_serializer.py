from rest_framework import serializers
from models import Patient



class PatientListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    gender = serializers.CharField()
    date_of_birth = serializers.DateField()


class PatientRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['phone']