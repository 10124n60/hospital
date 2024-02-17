from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, filters
from models import Patient
from api.serializers.patient_serializer import PatientCreateSerializer, PatientListSerializer, PatientRetriveSerializer, PatientUpdateSerializer

from api.mixins import HospitalGenericViewSet


class PatientView(
    HospitalGenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
):
 

 lookup_field = 'id'

 filter_backends = [DjangoFilterBackend, filters.SearchFilter]

 filterset_fields = ['first_name','last_name']

 search_fields = ['first_name','last_name']

 def get_action_permissions(self):
     if self.action in ('list', 'retrieve'):
        self.action_permissions = ['view_patient',]
     elif self.action == 'create':
        self.action_permissions = ['create_patient',]
     elif self.action == 'update':
        self.action_permissions = ['update_patient',]
     elif self.action == 'destroy':
        self.action_permissions = ['delete_patient',]
         
 

 def get_serializer_class(self):
     if self.action == 'list':
         return PatientListSerializer
     if self.action == 'retrieve':
         return PatientRetriveSerializer
     if self.action == 'create':
         return PatientCreateSerializer
     if self.action == 'update':
         return PatientUpdateSerializer
    

 def get_queryset(self):    
     return Patient.objects.all()
     
    