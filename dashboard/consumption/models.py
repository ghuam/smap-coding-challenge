# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    id = models.IntegerField("UserID", primary_key=True)
    area = models.CharField("AreaID", max_length=2)
    tariff = models.CharField("TariffID", max_length=2)

    def to_dict(self):
        obj = {'id': self.id,
               'area': self.area,
               'tariff': self.tariff}
        return obj

class Consumption(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    time = models.DateTimeField("Timestamp")
    units = models.FloatField("Usage")

    def to_dict(self):
        obj = {'datetime': self.time.strftime("%Y-%m-%d %H:%M:%S"),
               'units': self.units,
               'user': self.user.id}
        return obj

    @classmethod
    def get_total_consumption(cls, user):
        total_consumption = 0.0
        consumption_list = Consumption.objects.filter(user=user)
        if len(consumption_list) == 0:
            return total_consumption
        for record in consumption_list:
            total_consumption = total_consumption + record.units
        return total_consumption