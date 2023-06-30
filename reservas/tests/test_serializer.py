from django.utils import timezone
from decimal import Decimal
from imoveis.models import Imovel
from anuncios.models import Anuncios
from reservas.models import Reservas
from reservas.serializers import ReservaSerializer
from django.test import TestCase


class ReservaSerializerTest(TestCase):
    def setUp(self):
        self.imovel = Imovel.objects.create(
            cod_imovel='cod_teste',
            limite_hospedes=2,
            qtd_banheiros=1,
            aceita_animais=True,
            valor_limpeza=Decimal('100.00'),
        )

        self.anuncio = Anuncios.objects.create(
            imovel=self.imovel,
            nome_plataforma='teste',
            taxa_plataforma=Decimal('10.00')
        )

        self.reserva_attributes = {
            'codigo_reserva': 'codigo_teste',
            'anuncio': self.anuncio,
            'check_in': timezone.now().date(),
            'check_out': (timezone.now() + timezone.timedelta(days=2)).date(),
            'preco_total': 200.0,
            'comentario': 'comentario_teste',
            'numero_hospedes': 2,
        }

        self.serializer = ReservaSerializer(instance=Reservas.objects.create(**self.reserva_attributes))

        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertCountEqual(self.data.keys(),
                              ['id', 'codigo_reserva', 'anuncio', 'check_in', 'check_out', 'preco_total', 'comentario',
                               'numero_hospedes', 'data_criacao', 'data_atualizacao'])

    def test_anuncio_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['anuncio'], self.reserva_attributes['anuncio'].id)

    def test_check_in_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['check_in'], self.reserva_attributes['check_in'].isoformat())

    def test_check_out_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['check_out'], self.reserva_attributes['check_out'].isoformat())

    def test_preco_total_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['preco_total'], self.reserva_attributes['preco_total'])

    def test_comentario_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['comentario'], self.reserva_attributes['comentario'])

    def test_numero_hospedes_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['numero_hospedes'], self.reserva_attributes['numero_hospedes'])
