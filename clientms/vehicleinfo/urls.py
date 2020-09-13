from django.urls import path
from .views import (
    VehicleinfoListView,
    VehicleinfoUpdateView,
    VehicleinfoDetailView,
    VehicleinfoDeleteView,
    VehicleinfoCreateView,
)


urlpatterns = [

    path('<int:pk>/edit/',
         VehicleinfoUpdateView.as_view(), name='vehicleinfo_edit'),
    path('<int:pk>/',
         VehicleinfoDetailView.as_view(), name='vehicleinfo_detail'),
    path('<int:pk>/delete/',
         VehicleinfoDeleteView.as_view(), name='vehicleinfo_delete'),
    path('', VehicleinfoListView.as_view(), name='vehicleinfo_list'),
    path('new/', VehicleinfoCreateView.as_view(), name='vehicleinfo_new'),
]
