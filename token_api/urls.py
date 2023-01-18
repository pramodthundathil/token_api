
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Home import urls
import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(Home.urls)),
]
