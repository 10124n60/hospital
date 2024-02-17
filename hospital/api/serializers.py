from rest_framework import serializers
from .models import Medic, Patient, Service, Spetiality, Visit


class MedicListSerializer(serializers.Serializer):
    full_name = serializers.CharField()


class MedicRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = '__all__'


class MedicCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = '__all__'


class MedicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medic
        fields = ['spetiality','phone']

class PatientListSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    gender = serializers.CharField()
    date_of_birth = serializers.DateField()



class ServiceListSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()


class ServiceRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ServiceUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['cost']


class VisitListSerializer(serializers.Serializer):
    planned_date = serializers.DateTimeField()
    status = serializers.CharField()
    service = serializers.CharField()


class VisitRetriveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = '__all__'


class VisitUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['status','notes']

