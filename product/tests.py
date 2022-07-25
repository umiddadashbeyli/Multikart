from django.test import TestCase
from product.models import *


class TestDiscountModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'value' : 10,
            'is_percentage' : 'True',
        }
        cls.discount = Discount.objects.create(**cls.data1)
    
    def test_created_data(self):
        discount = Discount.objects.first()
        self.assertEqual(discount.value, self.data1['value'])

    @classmethod
    def tearDownClass(cls):
        Discount.objects.first().delete()
        del cls.discount
        del cls.data1


class TestCategoryModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.category = Category.objects.create(**cls.data1)
    
    def test_created_data(self):
        category = Category.objects.first()
        self.assertEqual(category.title, self.data1['title'])

    def test_str_method(self):
        self.assertEqual(str(self.category), self.data1['title'])

    @classmethod
    def tearDownClass(cls):
        Category.objects.first().delete()
        del cls.category
        del cls.data1

class TestPropertyModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.category = Category.objects.create(**cls.data1)


        cls.data2 = {
            'title' : 'Color',
            'category' : cls.category,
        }
        cls.property = Property.objects.create(**cls.data2)

    
    def test_created_data(self):
        property = Property.objects.first()
        self.assertEqual(str(property.category), self.data1['title'])

    @classmethod
    def tearDownClass(cls):
        Property.objects.first().delete()
        del cls.category
        del cls.property
        del cls.data1
        del cls.data2


class TestPropertyValueModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.category = Category.objects.create(**cls.data1)

        cls.data2 = {
            'title' : 'Color',
            'category' : cls.category,
        }
        cls.property = Property.objects.create(**cls.data2)


        cls.data3 = {
            'title' : 'Blue',
            'property' : cls.property,
        }
        cls.property_value = PropertyValue.objects.create(**cls.data3)

    
    def test_created_data(self):
        property_value = PropertyValue.objects.first()
        self.assertEqual(str(property_value.property), self.data2['title'])

    @classmethod
    def tearDownClass(cls):
        PropertyValue.objects.first().delete()
        del cls.category
        del cls.property
        del cls.property_value
        del cls.data1
        del cls.data2
        del cls.data3


class TestProductModel(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data1 = {
            'title' : 'Shoes',
        }
        cls.category = Category.objects.create(**cls.data1)

        cls.data2 = {
            'title' : 'Color',
            'category' : cls.category,
        }
        cls.property = Property.objects.create(**cls.data2)


        cls.data3 = {
            'title' : 'Blue',
            'property' : cls.property,
        }
        cls.property_value = PropertyValue.objects.create(**cls.data3)

        cls.data4 = {
            'value' : 10,
            'is_percentage' : 'True',
        }
        cls.discount = Discount.objects.create(**cls.data4)

        cls.data5 = {
            'title' : 'Gros',
            'price' : 20,
            'discount' : cls.discount,
            'property_value' : cls.property_value,
            # 'category' : cls.category
        }
        cls.product = Product.objects.create(**cls.data5)

    
    def test_created_data(self):
        product = Product.objects.first()
        self.assertEqual(product.discount.value, self.data4['value'])
        self.assertEqual(str(product.property_value), self.data3['title'])
        # self.assertEqual(product.category.all()[0], self.data1['title'])

    @classmethod
    def tearDownClass(cls):
        Product.objects.first().delete()
        del cls.category
        del cls.property
        del cls.property_value
        del cls.discount
        del cls.product
        del cls.data1
        del cls.data2
        del cls.data3

