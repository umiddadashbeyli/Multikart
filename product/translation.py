from modeltranslation.translator import translator, TranslationOptions
from product.models import Category, Product


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'price',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)