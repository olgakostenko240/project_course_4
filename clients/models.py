from django.db import models


class Clients(models.Model):
    email = models.EmailField(
        unique=True, verbose_name="Почта", help_text="Введите свою почту"
    )
    full_name = models.CharField(
        max_length=150,
        verbose_name="Ф.И.О.",
        help_text="Введите свое фио",
        blank=True,
        null=True,
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        help_text="Введите комментарий",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.email} {self.full_name}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ["email", "full_name"]


class Message(models.Model):
    topic = models.CharField(
        max_length=150, verbose_name="Тема письма", help_text="Введите тему письма"
    )
    body = models.TextField(verbose_name="Тело письма", help_text="Введите тело письма")

    def __str__(self):
        return f"{self.topic} {self.body}"

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["topic"]


class Campaign(models.Model):
    STATUS_CHOICES = [
        ("created", "Создана"),
        ("started", "Запущена"),
        ("completed", "Завершена"),
    ]

    first_sent_time = models.DateTimeField(
        verbose_name="Дата первой отправки",
        help_text="Введите дату первой отправки",
        null=True,
        blank=True,
    )
    end_time = models.DateTimeField(
        verbose_name="Дата окончания отправки",
        help_text="Введите дату окончания отправки",
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="created",
        verbose_name="Статус",
        help_text="Введите статус",
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        verbose_name="Сообщение",
        related_name="message",
    )
    is_active = models.BooleanField(default=True, verbose_name="активна")
    recipients = models.ManyToManyField(Clients, verbose_name="Получатели")
    successful_attempts = models.IntegerField(default=0)
    unsuccessful_attempts = models.IntegerField(default=0)
    sent_messages = models.IntegerField(default=0)

    def __str__(self):
        return f"Рассылка {self.first_sent_time} - {self.status}"

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"
        ordering = ["-end_time"]


class CampaignAttempt(models.Model):
    STATUS_CHOICES = [
        ("status_ok", "Успешно"),
        ("status_nok", "Не успешно"),
    ]

    date_attempt = models.DateTimeField(verbose_name="Дата и время попытки")
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, verbose_name="Статус попытки"
    )
    server_response = models.TextField(verbose_name="Ответ почтового сервера")
    campaign = models.ForeignKey(
        Campaign,
        on_delete=models.CASCADE,
        verbose_name="Рассылка",
        related_name="campaign",
    )

    def __str__(self):
        return f"{self.date_attempt} <{self.status}>"

    class Meta:
        verbose_name = "Попытка"
        verbose_name_plural = "Попытки"
        ordering = ["date_attempt", "status"]
