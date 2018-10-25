from __future__ import absolute_import
from celery import shared_task
import time
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_mail_util(subject, text, email, fail_silently=False):
    print('start send email to %s ...' % email)
    send_mail(
        subject, 
        '', 
        settings.EMAIL_HOST_USER, 
        [email], 
        fail_silently=fail_silently,
        html_message=text
        )
    print('send email success')