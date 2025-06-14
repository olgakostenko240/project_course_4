from django.shortcuts import render
from clients.models import Clients
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from clients.forms import ClientsForm


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
