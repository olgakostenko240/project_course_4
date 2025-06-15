from clients.models import Clients, Message, Campaign
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clients.forms import ClientsForm, MessageForm, CampaignForm


class ClientListView(ListView):
    model = Clients


class ClientDetailView(DetailView):
    model = Clients


class ClientCreateView(CreateView):
    model = Clients
    form_class = ClientsForm
    # fields = ("email", "full_name", "comment")
    success_url = reverse_lazy('clients:clients_list')


class ClientUpdateView(UpdateView):
    model = Clients
    form_class = ClientsForm
    # fields = ("email", "full_name", "comment")
    success_url = reverse_lazy('clients:clients_list')


class ClientDeleteView(DeleteView):
    model = Clients
    success_url = reverse_lazy('clients:clients_list')


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('clients:message_list')


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('clients:message_list')


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('clients:message_list')


class CampaignListView(ListView):
    model = Campaign


class CampaignDetailView(DetailView):
    model = Campaign


class CampaignCreateView(CreateView):
    model = Campaign
    form_class = CampaignForm
    success_url = reverse_lazy('clients:campaign_list')


class CampaignUpdateView(UpdateView):
    model = Campaign
    form_class = CampaignForm
    success_url = reverse_lazy('clients:campaign_list')


class CampaignDeleteView(DeleteView):
    model = Campaign
    success_url = reverse_lazy('clients:campaign_list')
