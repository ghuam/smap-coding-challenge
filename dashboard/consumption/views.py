# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import dashboard.settings
from models import User, Consumption
import os, csv

# Create your views here.


def summary(request):
    input_data = []
    columns = ['id', 'area', 'tariff']
    user_consumption_data = []
    users = User.objects.all()
    for user in users:
        user_consumption_data.append({'id'                : user.id,
                                      'total_consumption' :
                                          Consumption.get_total_consumption(user)})
        input_data.append(user.to_dict())
    context = {
        'user_data'   : input_data,
        'column_names': columns,
        "chart_title" : "Total consumption by user",
        "data_points" : user_consumption_data,
    }
    return render(request, 'consumption/summary.html', context)


def detail(request):
    context = {
    }
    return render(request, 'consumption/detail.html', context)
