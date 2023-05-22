from django.db import models


class Weather(models.Model):
    locality = models.CharField('Город', max_length=255)
    lat = models.FloatField('Широта')
    lon = models.FloatField('Долгота')
    now_dt = models.DateTimeField('Дата запроса', auto_now_add=True)
    data = models.JSONField()

    class Meta:
        ordering = ['now_dt']
        verbose_name = 'Погода'
        verbose_name_plural = 'Список прогноза погоды'

    def __str__(self):
        return f'{self.locality}'



