from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from product.models import (Discount, Category, Property, PropertyValue, ProductPropertyValue, 
                            Product, Shipping, Brand, Image, Review, Tag)



admin.site.register([Discount, Shipping, Property, PropertyValue, ProductPropertyValue, 
                    Brand, Image, Review, Tag])
# class ProductAdmin(admin.ModelAdmin):
#     list_display =  ('title', 'price')
#     list_filter = ('price',)



@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    pass

# admin.site.register(Product, ProductAdmin)