from django.test import TestCase
from orders.models import Order
from django.urls import reverse

from django.shortcuts import render, get_object_or_404


class AuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Order.objects.create(first_name='Big', last_name='Bob')

    def test_first_name_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'Имя')

    def test_email(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'email')


