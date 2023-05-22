from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from dadata import Dadata
import requests
from core import forms
from core import models
from core import filter
import subprocess
from django.conf import settings


class Index(View):
    template_name = 'core/index.html'

    def get(self, request):
        form_coordinate = forms.Coordinate()
        form_adress = forms.Adress()
        return render(request, 'core/index.html', {
            'form_coordinate': form_coordinate,
            'form_adress': form_adress
        })


def coordinate_parser(request):
    if request.method == 'POST':
        form = forms.Coordinate(request.POST)
        if form.is_valid():
            lat = form.cleaned_data['lat']
            lon = form.cleaned_data['lon']
            count = form.cleaned_data['count']
            url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&lang=ru_RU&limit={count}&hours=False&extra=False"
            headers = {'X-Yandex-API-Key': 'cba435bc-4c93-4199-98ce-61eac91e6485'}
            qs_parser = requests.get(url, headers=headers).json()
            weather_data = models.Weather.objects.create(
                lat=qs_parser['info']['lat'],
                lon=qs_parser['info']['lon'],
                locality=qs_parser['geo_object']['locality']['name'],
                data=qs_parser,
            )
            return render(request, 'core/coordinate.html', {'form': form, 'qs': weather_data})
        else:
            form = forms.Coordinate()
        return render(request, 'core/coordinate.html', {'form': form})


def adress_parser(request):
    if request.method == 'POST':
        form = forms.Adress(request.POST)
        if form.is_valid():
            token = "fca6c19785de791434a2e49a0521ec0182c8ae10"
            secret = "c046af9d277ee16ad34c206e8d925652d73dfaa2"
            dadata = Dadata(token, secret)
            address = request.POST.get('adress')
            result = dadata.clean("address", address)
            lat = result.get('geo_lat')
            lon = result.get('geo_lon')
            count = form.cleaned_data['count']
            url = f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&lang=ru_RU&limit={count}&hours=False&extra=False"
            headers = {'X-Yandex-API-Key': 'cba435bc-4c93-4199-98ce-61eac91e6485'}
            qs_parser = requests.get(url, headers=headers).json()
            weather_data = models.Weather.objects.create(
                lat=qs_parser['info']['lat'],
                lon=qs_parser['info']['lon'],
                locality=qs_parser['geo_object']['locality']['name'],
                data=qs_parser,
            )

            return render(request, 'core/adress.html', {'form': form, 'qs': weather_data})
    else:
        form = forms.Adress()
    return render(request, 'core/adress.html', {'form': form})


class history_weather(ListView):
    template_name = 'core/history_weather.html'
    queryset = models.Weather.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        c = super().get_context_data(**kwargs)
        c['filter'] = filter.WeatherFilter(self.request.GET, queryset=models.Weather.objects.all())
        c['form'] = forms.Searh_history()
        return c


class weather_delail(ListView):
    template_name = 'core/weather_detail.html'

    def get_queryset(self):
        return models.Weather.objects.filter(id=self.request.GET.get('pk'))

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        p = self.get_queryset().get()
        c['qs'] = p
        return c


def converter(request):
    if request.method == 'POST':
        form = forms.Text(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            name = form.cleaned_data['name']
            command = f'espeak -vru -w {settings.STATIC_ROOT}/{name}.wav "{text}"'
            subprocess.call(command, shell=True)
            audio_file = f'core/audio/{name}.wav'
            return render(request, 'core/converter.html', {'form': form, 'file_path': audio_file})
    else:
        form = forms.Text()
    return render(request, 'core/converter.html', {'form': form})







