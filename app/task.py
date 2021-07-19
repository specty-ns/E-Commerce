from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_accept():
    send_mail('Celery',"Worked","e.plastic.aans@gmail.com",["nihirshah34@gmail.com"],
        fail_silently=False
        )
    return None


@shared_task
def send_mail_reject():
    send_mail('Celery',"Reject","e.plastic.aans@gmail.com",["nihirshah34@gmail.com"],
        fail_silently=False
        )
    return None