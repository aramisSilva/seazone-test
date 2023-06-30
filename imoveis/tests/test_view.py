from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from ..models import Imovel
from django.contrib.auth.models import User
from decimal import Decimal


class ImovelViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='test', password='test')
        cls.client = APIClient()
        cls.client.force_authenticate(user=cls.user)
        cls.imovel = Imovel.objects.create(
            cod_imovel='001',
            limite_hospedes=4,
            qtd_banheiros=1,
            aceita_animais=True,
            valor_limpeza=Decimal('100.00')
        )

    def test_get_all_imoveis(self):
        response = self.client.get(reverse('imovel-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['cod_imovel'], '001')

    def test_get_single_imovel(self):
        response = self.client.get(reverse('imovel-detail', kwargs={'pk': self.imovel.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cod_imovel'], '001')

    def test_create_imovel(self):
        response = self.client.post(reverse('imovel-list'), {
            'cod_imovel': '002',
            'limite_hospedes': 5,
            'qtd_banheiros': 2,
            'aceita_animais': False,
            'valor_limpeza': '150.00'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_imovel(self):
        response = self.client.put(reverse('imovel-detail', kwargs={'pk': self.imovel.pk}), {
            'cod_imovel': '001',
            'limite_hospedes': 4,
            'qtd_banheiros': 2,
            'aceita_animais': True,
            'valor_limpeza': '150.00'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['qtd_banheiros'], 2)

    def test_destroy_imovel(self):
        response = self.client.delete(reverse('imovel-detail', kwargs={'pk': self.imovel.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
