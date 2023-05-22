from django import forms
from core import models


class Coordinate(forms.Form):
    lat = forms.FloatField(label='Ширина', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                         'placeholder': 'Введите ширину'
                                                                         }))
    lon = forms.FloatField(label='Долгота', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Введите долготу'
                                                                          }))

    count = forms.IntegerField(label='Прогноз', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                          'placeholder': 'Введите колличество дней'
                                                                          }))


class Adress(forms.Form):
    adress = forms.CharField(max_length=255, label='Адрес', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите Адрес'
        }))
    count = forms.IntegerField(label='Прогноз', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Введите колличество дней'
                                                                              }))


class Searh_history(forms.Form):
    locality = forms.CharField(max_length=255, label='Город', required=False,)
    now_dt = forms.DateTimeField(label='Дата', required=False, widget=forms.DateTimeInput(
        attrs={
            'type': 'datetime-local',
            'format': '%Y-%m-%dT%H:%M'
        }))


class Text(forms.Form):
    text = forms.CharField(max_length=255, label='Текст', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите содержание'
        }))

    name = forms.CharField(max_length=255, label='Файл', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя файла'
        }))





