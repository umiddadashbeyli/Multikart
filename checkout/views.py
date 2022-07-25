from django.shortcuts import redirect, render
from checkout.forms import CheckoutForm
from core.forms import SubscriberForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


def checkout (request):
    form = CheckoutForm()
    form1 = SubscriberForm()
    if request.method == 'POST':
        form = CheckoutForm(data = request.POST)
        form1 = SubscriberForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('checkout'))
        elif form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form,
        'form1' : form1
    }
    return render(request, 'checkout.html', context)

def success (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'order-success.html', context)


@login_required
def wishlist (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'wishlist.html', context)