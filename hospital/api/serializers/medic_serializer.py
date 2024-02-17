from rest_framework import serializers
from models import Medic


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