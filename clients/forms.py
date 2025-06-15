from django.forms import ModelForm, BooleanField

from clients.models import Clients, Message, Campaign


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ClientsForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Clients
        fields = "__all__"


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class CampaignForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Campaign
        exclude = ("is_active", "successful_attempts", "unsuccessful_attempts", "sent_messages",)
