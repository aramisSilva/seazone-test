from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from ..models import Anuncios, Imovel
from ..serializers import AnunciosSerializer
from django.contrib.auth.models import User


class AnuncioViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.imovel = Imovel.objects.create(cod_imovel='001', limite_hospedes=4, qtd_banheiros=1, valor_limpeza=100.00, aceita_animais=True)
        cls.anuncio = Anuncios.objects.create(imovel=cls.imovel, nome_plataforma='Airbnb', taxa_plataforma=10.00)
        cls.user = User.objects.create_user(username='test', password='test')

    def setUp(self):
        self.client = APIClient()
        login = self.client.login(username='test', password='test')
        assert login, "login failed"

    def test_get_all_anuncios(self):
        response = self.client.get(reverse('anuncios-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['nome_plataforma'], 'Airbnb')

    def test_get_single_anuncio(self):
        response = self.client.get(reverse('anuncios-detail', kwargs={'pk': self.anuncio.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_plataforma'], 'Airbnb')

    def test_create_anuncio(self):
        response = self.client.post(reverse('anuncios-list'), {
            'imovel': self.imovel.pk,
            'nome_plataforma': 'Booking',
            'taxa_plataforma': 10.00
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_anuncio(self):
        response = self.client.put(reverse('anuncios-detail', kwargs={'pk': self.anuncio.pk}), {
            'imovel': self.imovel.pk,
            'nome_plataforma': 'Booking',
            'taxa_plataforma': 15.00
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_plataforma'], 'Booking')

    def test_destroy_anuncio(self):
        response = self.client.delete(reverse('anuncios-detail', kwargs={'pk': self.anuncio.pk}))
        self.assertEqual(response.status_code, status.HTTP_406_NOT_ACCEPTABLE)

