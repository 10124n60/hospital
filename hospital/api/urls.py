from django.contrib import admin
from django.urls import path
from .views import MedicView,PatientView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('medic/',MedicView.as_view({'get':'list', 'post':'create'})),
    path('medic/<int:id>/',MedicView.as_view({'get':'retrieve', 'put':'update'})),
    path('medic/<int:id>/patient/',MedicView.as_view({'get':'list_patient'})),

    path('patient/',MedicView.as_view({'get':'list', 'post':'create'})),
    path('patient/<int:id>/',MedicView.as_view({'get':'retrieve', 'put':'update'})),

##    path('visits/',VisitView.as_view({'get':'list', 'post':'create'})),
##    path('visits/<int:id>/',VisitView.as_view({'get':'retrieve', 'put':'update'})),

##    path('service/',ServiceView.as_view({'get':'list', 'post':'create'})),
##    path('service/<int:id>/',ServiceView.as_view({'get':'retrieve', 'put':'update'})),
    

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
