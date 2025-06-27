import secrets

from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.utils.crypto import get_random_string

from config.settings import EMAIL_HOST_USER
from users.models import User
from users.forms import UserRegisterForm, PasswordRecoveryForm
from django.core.mail import send_mail


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Здравствуйте, перейдите по ссылке для подтверждения почты: {url} ",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


class PasswordRecoveryView(FormView):
    template_name = "password_recovery.html"
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy("users:password_reset_done")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        user = User.objects.get(email=email)
        length = 12
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        password = get_random_string(length, alphabet)
        user.set_password(password)
        user.save()
        send_mail(
            subject="Восстановление пароля",
            message=f"Ваш новый пароль: {password}, для подтверждения пароля передите по ссылке и войдите под новым поролем http://127.0.0.1:8000/users/password-reset/complete/",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False,
        )
        return super().form_valid(form)
