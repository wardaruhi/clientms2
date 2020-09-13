from django.contrib import admin
from .models import VehicleInfo


class VehicleInfoAdmin(admin.ModelAdmin):
    model = VehicleInfo

admin.site.register(VehicleInfo, VehicleInfoAdmin)
