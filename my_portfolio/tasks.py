from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task():
    send_mail('Celery task worked', 'Lorem', 'kimvolodymyr1@gmail.com', ['kimvladimirgsu@gmail.com'])
    return None
