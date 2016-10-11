from django.test import TestCase
from django.template import Context, Template


class TagTests(TestCase):
    def test_tag(self):
        template = "{{ preco|currency }}"
        t = Template('{% load currency %}'+template)
        c = Context({'preco': 20})
        self.assertEqual(t.render(c), "R$ 20,00")