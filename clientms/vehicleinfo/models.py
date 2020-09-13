from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class VehicleInfo(models.Model):
    companymake = models.CharField(max_length=50,blank=False, null=False, default='')
    model_number = models.CharField(max_length=50, blank=True, null=True,default='')
    VIN_number = models.CharField(max_length=50,blank=True, null=True, default='')
    date_of_purchase = models.DateField(blank=True, null=True, default=timezone.now())
    date_of_last_service = models.DateField(blank=True, null=True, default=timezone.now())
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def _str_(self):
        return self.make

    def get_absolute_url(self):
        return reverse('vehicleinfo_detail', args=[str(self.id)])
