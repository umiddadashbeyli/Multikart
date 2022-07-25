from django.contrib.auth import get_user_model
from django.db import models
from product.models import *


USER = get_user_model()

class Subscriber(models.Model):
    email = models.EmailField(max_length=50)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscriber'
    
    def __srt__(self):
        return self.email

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    your_mesaage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.first_name


class Basket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'

    # @property
    # def get_cart_total(self):
    #     basketitems = BasketItem.objects.filter(basket = self)
    #     total = sum([item.get_total for item in basketitems])
    #     return total




class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    data_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Basket Item'
        verbose_name_plural = 'Basket Items'

    @property
    def get_total(self):
        total = float(self.product.price) * self.quantity
        return total
