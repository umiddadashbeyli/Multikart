from django.urls import path
from . import views

urlpatterns = [
    path('error/', views.error, name='error'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('home/', views.home, name='home'),
]