from django.urls import path
from clients.apps import ClientsConfig
from clients.views import home

app_name = ClientsConfig.name

urlpatterns = [path("", home, name="home")]
