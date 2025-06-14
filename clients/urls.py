from django.urls import path
from clients.apps import ClientsConfig
from clients.views import (ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
                           MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView)

app_name = ClientsConfig.name

urlpatterns = [
    path("", ClientListView.as_view(), name="clients_list"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="clients_detail"),
    path("clients/create/", ClientCreateView.as_view(), name="clients_create"),
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="clients_update"),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="clients_delete"),

    path("message/", MessageListView.as_view(), name="message_list"),
    path("message/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("message/create/", MessageCreateView.as_view(), name="message_create"),
    path("message/<int:pk>/update/", MessageUpdateView.as_view(), name="message_update"),
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete")
]
