from django.contrib import admin

from clients.models import Clients, Message, Campaign


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "full_name")
    search_fields = ("email", "full_name")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "topic",)
    search_fields = ("topic",)


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("id", "status",)
    search_fields = ("status",)
