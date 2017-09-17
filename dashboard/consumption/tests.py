# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client

# Create your tests here.
class ConsumptionTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_summary(self):
        response = self.client.get("/summary/")
        self.assertEqual(response.status_code, 200)

        #  Response must be rendered with 'layout.html', and 'summary.html'
        self.assertEqual(len(response.templates), 2)
