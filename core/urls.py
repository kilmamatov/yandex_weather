from django.urls import path
import core.views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', core.views.Index.as_view()),
    path('coordinate_parser/', core.views.coordinate_parser),
    path('adress_parser/', core.views.adress_parser),
    path('history_weather/', core.views.history_weather.as_view()),
    path('weather_delail/', core.views.weather_delail.as_view()),
    path('converter/', core.views.converter),
]

urlpatterns += static(settings.STATIC_ROOT, document_root=settings.STATIC_ROOT)
