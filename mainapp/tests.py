from django.test import TestCase

from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from mainapp.models import Product, ProductCategory


class TestMainappSmoke(TestCase):
    # fixtures = ['authapp.json', 'mainapp.json', 'basketapp.json', 'ordersapp.json']
    fixtures = ['mainapp.json']

    # @classmethod
    # def setUpClass(cls): # once
    # super().setUpClass()
    # cls.client = Client()

    # @classmethod
    # def tearDownClass(cls): # once
    # pass

    def setUp(self):
        self.client = Client()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('main:products'))
        self.assertEqual(response.status_code, 200)

    def test_product_category_urls(self):
        response = self.client.get(reverse('main:catalog', kwargs={'pk': 0}))
        self.assertEqual(response.status_code, 200)
        for category in ProductCategory.objects.all():
            response = self.client.get(reverse('main:catalog', kwargs={'pk': category.pk}))
            self.assertEqual(response.status_code, 200)

    def test_product_urls(self):
        for product in Product.objects.all():
            response = self.client.get(f'/product/{product.pk}/')
            self.assertEqual(response.status_code, 200)
