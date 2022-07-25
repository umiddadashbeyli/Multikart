from django.shortcuts import render, redirect
from core.forms import SubscriberForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required





def error (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, '404.html', context)

def about (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'about-page.html', context)

@login_required
def contact (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'contact.html', context)

def faq (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'faq.html', context)

def home (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form1' : form1
    }
    return render(request, 'index.html', context)



