from modeltranslation.translator import translator, TranslationOptions
from core.models import Basket, BasketItem


class BasketTranslationOptions(TranslationOptions):
    fields = ('user',)


class BasketItemTranslationOptions(TranslationOptions):
    fields = ('basket', 'product')


translator.register(Basket, BasketTranslationOptions)
translator.register(BasketItem, BasketItemTranslationOptions)