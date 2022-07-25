from django.contrib.auth import get_user_model
from django.db import models



USER = get_user_model()


class Checkout(models.Model):

    Countries = [('Aze', 'Azerbaijan'), ('Tur', 'Turkey')]

    first_name = models.CharField(max_length=30, verbose_name='First Name')
    last_name = models.CharField(max_length=30, verbose_name='Last Name')
    email = models.EmailField(max_length=30, verbose_name='Email Adress', unique=True)
    phone_number = models.CharField(max_length=15, verbose_name='Phone')
    country = models.CharField(max_length=3, choices=Countries, default=Countries[0][0], verbose_name='Counrty')
    adress = models.CharField(max_length=50, verbose_name='Adress')
    city = models.CharField(max_length=50, verbose_name='City/Town')
    state = models.CharField(max_length=50, null=True, verbose_name='State/Counrty')
    postal_code = models.CharField(max_length=10, verbose_name='Postal Code')
    create_an_account = models.BooleanField(default=False, verbose_name='Create an Account?')
    free_shipping = models.BooleanField(default=False, verbose_name='Free Shipping')
    local_pickup = models.BooleanField(default=False, verbose_name='Local Pickup')



    class Meta:
        verbose_name = 'Checkout'
        verbose_name_plural = 'Checkout'

    def __srt__(self):
        return self.user