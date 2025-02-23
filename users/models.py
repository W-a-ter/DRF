from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import Course, Lesson


class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Payment(models.Model):
    """Модель оплаты курса/урока."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", verbose_name="пользователь", default=None, null=True,
        blank=True
    )
    date_pay = models.DateTimeField(verbose_name="Дата оплаты", auto_now_add=True, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс", blank=True, null=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="урок", blank=True, null=True)
    amount = models.PositiveIntegerField(verbose_name="сумма оплаты", null=True, blank=True)
    payment_method = models.CharField(
        max_length=16,
        choices=[("Наличными", "Наличными"), ("Перевод на карту", "Перевод на карту")],
        verbose_name="Способ оплаты", null=True, blank=True
    )
    session_id = models.CharField(max_length=255, verbose_name="id сессии", blank=True, null=True)
    link = models.URLField(max_length=400, verbose_name="ссылка на оплату", blank=True, null=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплаты"
