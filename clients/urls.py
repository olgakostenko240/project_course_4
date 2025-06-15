from django.urls import path
from clients.apps import ClientsConfig
from clients.views import (ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
                           MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView,
                           CampaignListView, CampaignDetailView, CampaignCreateView, CampaignUpdateView, CampaignDeleteView)

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
    path("message/<int:pk>/delete/", MessageDeleteView.as_view(), name="message_delete"),

    path("campaign/", CampaignListView.as_view(), name="campaign_list"),
    path("campaign/<int:pk>/", CampaignDetailView.as_view(), name="campaign_detail"),
    path("campaign/create/", CampaignCreateView.as_view(), name="campaign_create"),
    path("campaign/<int:pk>/update/", CampaignUpdateView.as_view(), name="campaign_update"),
    path("campaign/<int:pk>/delete/", CampaignDeleteView.as_view(), name="campaign_delete")
]
