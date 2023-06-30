from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from reservas.models import Reservas
from anuncios.models import Anuncios, Imovel


class ReservasModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        imovel = Imovel.objects.create(
            cod_imovel='001',
            limite_hospedes=4,
            qtd_banheiros=1,
            valor_limpeza=100.00,
            aceita_animais=True
        )
        cls.anuncio = Anuncios.objects.create(
            imovel=imovel,
            nome_plataforma='Airbnb',
            taxa_plataforma=10.00
        )

    def test_create_reservation(self):
        reserva = Reservas.objects.create(
            anuncio=self.anuncio,
            check_in=datetime.today(),
            check_out=datetime.today() + timedelta(days=1),
            preco_total=100.00,
            numero_hospedes=2
        )
        self.assertEqual(reserva.anuncio, self.anuncio)
        self.assertEqual(reserva.numero_hospedes, 2)
        self.assertEqual(reserva.preco_total, 100.00)

    def test_check_in_data_maior_que_check_out(self):
        with self.assertRaises(ValidationError):
            reserva = Reservas(
                anuncio=self.anuncio,
                check_in=datetime.today(),
                check_out=datetime.today() - timedelta(days=1),
                preco_total=100.00,
                numero_hospedes=2
            )
            reserva.clean()

    def test_auto_fields(self):
        reserva = Reservas.objects.create(
            anuncio=self.anuncio,
            check_in=datetime.today(),
            check_out=datetime.today() + timedelta(days=1),
            preco_total=100.00,
            numero_hospedes=2
        )
        self.assertIsNotNone(reserva.data_criacao)
        self.assertIsNotNone(reserva.data_atualizacao)
        self.assertIsNotNone(reserva.codigo_reserva)
        self.assertTrue(isinstance(reserva.data_criacao, datetime))