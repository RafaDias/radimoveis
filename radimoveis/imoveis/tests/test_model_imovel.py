from django.test import TestCase
from radimoveis.imoveis.models import Imovel


class ImovelModelTest(TestCase):
    def setUp(self):
        self.imovel = Imovel.objects.create(
            breve_descricao='Imóvel bacana',
            endereco='Av Brasil',
            preco=20.00
        )

    def test_create(self):
        self.assertTrue(Imovel.objects.exists())

    def test_str(self):
        self.assertEqual('Imóvel bacana', str(self.imovel))