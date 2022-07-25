from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from core.forms import SubscriberForm
from django.contrib.auth.decorators import login_required
from product.forms import ReviewForm
from product.models import Category, Product, PropertyValue, Property, Image, Brand, Review, Discount
from core.models import Basket, BasketItem
from django.views.generic.edit import FormMixin
from django.http import JsonResponse
import json
# Create your views here.



class CartListView(ListView):
    model = BasketItem
    template_name = 'cart.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['basket'] = Basket.objects.filter(user = self.request.user)
        return context
    

# def category (request):
#     form1 = SubscriberForm()
#     if request.method == 'POST':
#         form1 = SubscriberForm(data = request.POST)
#         if form1.is_valid():
#             form1.save()
#             return redirect(reverse_lazy('home'))
#     context = {
#         'form1' : form1
#     }
#     return render(request, 'category-page.html', context)

class ProductListView(ListView):
    model = Product
    template_name = 'category-page.html'
    context_object_name = 'products'
    success_url = 'product'


class ProductDetailView(FormMixin, DetailView):
    model = Product
    template_name = 'product-page.html'
    form_class = ReviewForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('product', kwargs={'pk': self.object.pk})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['brands'] = Brand.objects.all()
        context['new_products'] = Product.objects.all().order_by('-id')[:3]
        context['images'] = Image.objects.filter(product__title = self.object)
        context['properties'] = Property.objects.all()
        context['property_values'] = PropertyValue.objects.filter(product__title = self.object)
        category = Category.objects.get(product__title = self.object)
        context['releated_products'] = Product.objects.filter(category__title = category)
        context['reviews'] = Review.objects.filter(product__title = self.object)
        context['discounts'] = Discount.objects.filter(product__title = self.object)
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.instance.product = self.object
            form.instance.author = request.user
            form.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        return render(request, self.template_name, {'form': form})



    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form=form)



def search (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'search.html', context)

def vendor (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'vendor-profile.html', context)

# def updateItem(request):
#     data = json.loads(request.body)
#     productId = data['productId']
#     action = data['action']
#     author = request.user
#     product = Product.objects.get(id=productId)
#     basket, created = Basket.objects.get_or_create(user = author)
#     basketItem, created = BasketItem.objects.get_or_create(basket = basket, product = product)


#     if action == 'add':
#         basketItem.quantity = (basketItem.quantity + 1)
#     elif action == 'remove':
#         basketItem.quantity = (basketItem.quantity - 1)

#     basketItem.save()

#     if basketItem.quantity <=0:
#         basketItem.delete()

#     return JsonResponse('Item was added', safe=False)