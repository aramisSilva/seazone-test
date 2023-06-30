from django.test import TestCase
from ..models import Anuncios, Imovel
from ..serializers import AnunciosSerializer


class AnunciosSerializerTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.imovel = Imovel.objects.create(cod_imovel='001', limite_hospedes=4, qtd_banheiros=1, valor_limpeza=100.00, aceita_animais=True)
        cls.anuncio = Anuncios.objects.create(imovel=cls.imovel, nome_plataforma='Airbnb', taxa_plataforma=10.00)

    def test_serialize(self):
        """Testa a serialização de um objeto Anuncios"""
        serializer = AnunciosSerializer(self.anuncio)
        expected_data = {
            'id': self.anuncio.id,
            'imovel': self.imovel.id,
            'nome_plataforma': 'Airbnb',
            'taxa_plataforma': '10.00',
            'data_criacao': self.anuncio.data_criacao.isoformat(),
            'data_atualizacao': self.anuncio.data_atualizacao.isoformat(),
        }
        self.assertDictEqual(serializer.data, expected_data)

    def test_deserialize_valid_data(self):
        """Testa a desserialização de dados válidos"""
        data = {
            'imovel': self.imovel.id,
            'nome_plataforma': 'Booking',
            'taxa_plataforma': 10.00,
        }
        serializer = AnunciosSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_deserialize_invalid_data(self):
        """Testa a desserialização de dados inválidos"""
        data = {
            'imovel': self.imovel.id,
            'nome_plataforma': '',
            'taxa_plataforma': 10.00,
        }
        serializer = AnunciosSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('nome_plataforma', serializer.errors)
