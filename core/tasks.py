from celery import shared_task 
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Subscriber
from product.models import Product


@shared_task
def send_mail_to_subscribers(user, current_site):
    email_list = Subscriber.objects.filter(is_active = True).values_list('email', flat=True)
    products = Product.objects.all()
    message = render_to_string('email-subscribers.html', {
                'products': products
            })
    subject = 'New product from out website'
    mail = EmailMultiAlternatives(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=email_list)
    mail.content_subtype = 'html'
    mail.send()