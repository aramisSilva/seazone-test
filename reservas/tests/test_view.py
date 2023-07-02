from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from anuncios.models import Anuncios, Imovel
from reservas.models import Reservas
from datetime import datetime, timedelta


class ReservaViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        imovel = Imovel.objects.create(
            cod_imovel='001',
            limite_hospedes=4,
            qtd_banheiros=1,
            valor_limpeza=100.00,
            aceita_animais=True
        )
        self.anuncio = Anuncios.objects.create(
            imovel=imovel,
            nome_plataforma='Airbnb',
            taxa_plataforma=10.00
        )

    def test_create_reservation(self):
        url = reverse('reservas-list') # Use the URL name for your ReservaViewSet here
        data = {
            "anuncio": self.anuncio.id,
            "check_in": datetime.today().strftime('%Y-%m-%d'),
            "check_out": (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d'),
            "preco_total": 100.00,
            "numero_hospedes": 2
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_reservation(self):
        reserva = Reservas.objects.create(
            anuncio=self.anuncio,
            check_in=datetime.today(),
            check_out=datetime.today() + timedelta(days=1),
            preco_total=100.00,
            numero_hospedes=2
        )
        url = reverse('reservas-detail', args=[reserva.id])
        data = {
            "preco_total": 200.00,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
