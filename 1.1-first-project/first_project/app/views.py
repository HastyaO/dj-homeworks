import os
import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная': reverse('home'),
        'Текущее время': reverse('time'),
        'Рабочая директория': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    current_dir = os.listdir('.')
    msg = f'Рабочая директория: {current_dir}'
    return HttpResponse(msg)