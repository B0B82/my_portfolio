from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_email_task(new_user):
    send_mail('Congratulations!', 'You registered!', 'kimvolodymyr1@gmail.com', [f"{new_user.email}"])
    return None
