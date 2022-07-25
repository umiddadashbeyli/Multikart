from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models import Contact, Basket, BasketItem , Subscriber

admin.site.register([Contact, Subscriber])

admin.site.site_header = 'Multikart'


@admin.register(Basket)
class BasketAdmin(TranslationAdmin):
    pass

@admin.register(BasketItem)
class BasketItemAdmin(TranslationAdmin):
    pass