from django.shortcuts import render
from rest_framework import generics, viewsets, mixins
from rest_framework.response import Response
from .models import Medic, Patient, Service, Spetiality, Visit
from .serializers import MedicCreateSerializer,MedicListSerializer,MedicRetriveSerializer,MedicUpdateSerializer,PatientListSerializer
from .serializers import ServiceListSerializer, ServiceRetriveSerializer, ServiceCreateSerializer, ServiceUpdateSerializer
from .serializers import VisitCreateSerializer, VisitListSerializer, VisitRetriveSerializer, VisitUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import MedicAccessPermission, HasPermissionByAuthenticatedUserRole, RoleBasedPermissionMixin
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MedicFilters


class MedicView(
    RoleBasedPermissionMixin,
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin
):
 
 permission_classes = [IsAuthenticated, HasPermissionByAuthenticatedUserRole]
 
 lookup_field = 'id'   
 
 filter_backends = [DjangoFilterBackend]

 filterset_fields = ['first_name', 'last_name', 'spetiality']

 filterset_class = MedicFilters


 def get_action_permissions(self):
     if self.action in ('list', 'retrieve'):
        self.action_permissions = ['view_medic',]
     elif self.action == 'list_patient':
        self.action_permissions = ['view_patient',]
     else:
         self.action_permissions=[]

 def get_serializer_class(self):
     if self.action == 'list':
         return MedicListSerializer
     if self.action == 'retrieve':
         return MedicRetriveSerializer
     if self.action == 'create':
         return MedicCreateSerializer
     if self.action == 'update':
         return MedicUpdateSerializer
     if self.action == 'list_patient':
         return PatientListSerializer
    

 def get_queryset(self):
     
     if self.action == 'list_patient':
         return Patient.objects.prefetch_related(
             'visits'
         ).all()
     
     return Medic.objects.all()
 

 def list_patient(self, request, id):
     queryset = self.get_queryset().filter(visits__doctor_id=id)

     serializer = self.get_serializer(queryset, many=True)

     return Response(data=serializer.data)

class VisitView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin
):
 lookup_field = 'id'   

 def get_serializer_class(self):
     if self.action == 'list':
         return VisitListSerializer
     if self.action == 'retrieve':
         return VisitRetriveSerializer
     if self.action == 'create':
         return VisitCreateSerializer
     if self.action == 'update':
         return VisitUpdateSerializer
     
 def get_queryset(self):
     return Visit.objects.all()



class ServiceView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin
):
 lookup_field = 'id'   

 def get_serializer_class(self):
     if self.action == 'list':
         return ServiceListSerializer
     if self.action == 'retrieve':
         return ServiceRetriveSerializer
     if self.action == 'create':
         return ServiceCreateSerializer
     if self.action == 'update':
         return ServiceUpdateSerializer
     
 def get_queryset(self):
     return Service.objects.all()

