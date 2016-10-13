from django.test import TestCase
from django.shortcuts import resolve_url as r


class DashboardTest(TestCase):
    def setUp(self):
        self.response = self.client.get(r('imoveis:dashboard'), follow=True)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)