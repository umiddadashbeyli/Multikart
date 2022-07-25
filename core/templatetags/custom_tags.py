from django.template import Library
from core.forms import SubscriberForm
from product.models import Category


register = Library()

@register.simple_tag
def get_form():
    return SubscriberForm

@register.simple_tag
def get_categories():
    context = {}
    parent_categories = Category.objects.filter(parent_category=None)
    context["parents"] = parent_categories
    context['subs'] = Category.objects.all()
    return  context
