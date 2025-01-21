import time
from datetime import timedelta

from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone

from config.settings import EMAIL_HOST_USER
from users.models import User


# from users.models import User


@shared_task
def send_mail_receiver(email: list):
    """Функция отправки сообщений всем кто подписан на курс, когда курс изменяется"""
    send_mail(subject="Материалы курса обновлены.",
              message="Вы подписаны на курс, который изменился, переходите на сайт для ознакомления!",
              from_email=EMAIL_HOST_USER,
              recipient_list=email)


@shared_task
def check_is_active_user():
    """Функция проверяет, что пользователь не заходил больше месяца и блокирует его"""
    today = timezone.now()
    last_month = today - timedelta(days=32)
    users = User.objects.all()

    for user in users:
        if user.last_login is not None and user.last_login < last_month:
            user.is_active = False
            user.save()