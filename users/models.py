from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=50, verbose_name="Юзернейм", help_text="Введите юзернейм"
    )
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите вашу почту"
    )
    phone_number = models.CharField(
        max_length=15,
        verbose_name="Номер телефона",
        help_text="Введите ваш номер телефона",
        blank=True,
        null=True,
    )
    avatar = models.ImageField(upload_to="media/avatars/", blank=True, null=True)
    country = models.CharField(
        max_length=50,
        verbose_name="Страна проживания",
        help_text="Введите вашу страну проживания",
        blank=True,
        null=True,
    )
    token = models.CharField(unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
