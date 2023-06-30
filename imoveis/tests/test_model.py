from django.test import TestCase
from ..models import Imovel
from django.utils import timezone
from datetime import datetime
from decimal import Decimal


class ImovelModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.imovel = Imovel.objects.create(
            cod_imovel='001',
            limite_hospedes=4,
            qtd_banheiros=2,
            aceita_animais=True,
            valor_limpeza=Decimal('50.00')
        )

    def test_str_representation(self):
        self.assertEqual(str(self.imovel), '001')

    def test_ativar_imovel(self):
        self.assertIsNone(self.imovel.data_ativacao)
        self.imovel.ativar_imovel()
        self.assertIsNotNone(self.imovel.data_ativacao)

    def test_create_imovel(self):
        imovel = Imovel.objects.create(
            cod_imovel='002',
            limite_hospedes=5,
            qtd_banheiros=3,
            aceita_animais=False,
            valor_limpeza=Decimal('70.00')
        )
        self.assertEqual(imovel.cod_imovel, '002')
        self.assertEqual(imovel.limite_hospedes, 5)
        self.assertEqual(imovel.qtd_banheiros, 3)
        self.assertEqual(imovel.aceita_animais, False)
        self.assertEqual(imovel.valor_limpeza, Decimal('70.00'))
        self.assertIsNone(imovel.data_ativacao)

    def test_auto_fields(self):
        now = timezone.make_aware(datetime.now())
        self.assertLess(self.imovel.data_criacao, now)
        self.assertLess(self.imovel.data_atualizacao, now)
