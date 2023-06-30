from django.test import TestCase
from datetime import datetime
from decimal import Decimal
from imoveis.models import Imovel
from ..models import Anuncios


class AnunciosTestCase(TestCase):
    def setUp(self):
        self.imovel = Imovel.objects.create(cod_imovel='001', limite_hospedes=4, qtd_banheiros=2, valor_limpeza=Decimal('100.00'), aceita_animais=True)
        self.anuncio = Anuncios.objects.create(imovel=self.imovel, nome_plataforma='Airbnb', taxa_plataforma=Decimal('10.00'))

    def test_str_representation(self):
        self.assertEqual(str(self.anuncio), self.imovel.cod_imovel)

    def test_data_criacao_auto_now_add(self):
        self.assertIsNotNone(self.anuncio.data_criacao)
        self.assertTrue(isinstance(self.anuncio.data_criacao, datetime))

    def test_data_atualizacao_auto_now(self):
        old_data_atualizacao = self.anuncio.data_atualizacao
        self.anuncio.nome_plataforma = 'Booking'
        self.anuncio.save()
        self.assertNotEqual(self.anuncio.data_atualizacao, old_data_atualizacao)
        self.assertTrue(isinstance(self.anuncio.data_atualizacao, datetime))

    def test_related_name_anuncios(self):
        self.assertEqual(self.imovel.anuncios.first(), self.anuncio)
