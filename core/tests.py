from django.test import TestCase
from core.models import *


class TestSubscriberModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'email' : 'dadashbeyli@gmail.com',
            'is_active' : 'True',
        }
        cls.subscriber = Subscriber.objects.create(**cls.data1)
    
    def test_created_data(self):
        subscriber = Subscriber.objects.first()
        self.assertEqual(subscriber.email, self.data1['email'])

    @classmethod
    def tearDownClass(cls):
        Subscriber.objects.first().delete()
        del cls.subscriber
        del cls.data1

class TestContactModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'first_name' : 'Umid',
            'last_name' : 'Dadashbeyli',
        }
        cls.contact = Contact.objects.create(**cls.data1)
    
    def test_created_data(self):
        contact = Contact.objects.first()
        self.assertEqual(contact.first_name, self.data1['first_name'])

    @classmethod
    def tearDownClass(cls):
        Contact.objects.first().delete()
        del cls.contact
        del cls.data1

    