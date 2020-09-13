from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import VehicleInfo
from django.urls import reverse_lazy

class VehicleinfoListView(ListView):
    model = VehicleInfo
    template_name = 'vehicleinfo_list.html'

class VehicleinfoDetailView(DetailView):
    model = VehicleInfo
    template_name = 'vehicleinfo_detail.html'
    login_url = 'login'

class VehicleinfoUpdateView(UpdateView):
    model = VehicleInfo
    fields = ('companymake', 'model_number', 'VIN_number', 'date_of_purchase', 'date_of_last_service')
    template_name = 'vehicleinfo_edit.html'
    success_url = reverse_lazy('vehicleinfo_list')

class VehicleinfoDeleteView(DeleteView):
    model = VehicleInfo
    template_name = 'vehicleinfo_delete.html'
    success_url = reverse_lazy('vehicleinfo_list')

class VehicleinfoCreateView(CreateView):
    model = VehicleInfo
    template_name = 'vehicleinfo.html'
    fields = ('companymake', 'model_number', 'VIN_number', 'date_of_purchase', 'date_of_last_service')
    success_url = reverse_lazy('vehicleinfo_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
