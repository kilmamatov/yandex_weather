from django.contrib import admin
from django.urls import path, include
import core.urls

urlpatterns = [
    path('', include(core.urls)),
    path('admin/', admin.site.urls),
]
