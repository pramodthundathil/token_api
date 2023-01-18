from django.urls import path
from .import views

urlpatterns = [
    path("TokenGenerator",views.TokenGenerator,name="TokenGenerator"),
    path("DataTest",views.DataTest,name="DataTest"),
    path("AllPatientView",views.AllPatientView,name="AllPatientView")
]
