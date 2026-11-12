from django.urls import path
from . import views

app_name = "generador"

urlpatterns = [
    path('', views.generador, name="inicio"),
]