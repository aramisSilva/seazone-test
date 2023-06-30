from django.test import TestCase
from rest_framework.exceptions import ValidationError
from ..serializers import ImovelSerializer
from ..models import Imovel


class ImovelSerializerTest(TestCase):
    def setUp(self):
        self.imovel_attributes = {
            'cod_imovel': '123ABC',
            'limite_hospedes': 4,
            'qtd_banheiros': 2,
            'aceita_animais': True,
            'valor_limpeza': 150.00,
            'data_ativacao': None,
        }

        self.imovel = Imovel.objects.create(**self.imovel_attributes)
        self.serializer = ImovelSerializer(instance=self.imovel)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertCountEqual(['id', 'cod_imovel', 'limite_hospedes', 'qtd_banheiros', 'aceita_animais', 'valor_limpeza',
                               'data_ativacao', 'data_criacao', 'data_atualizacao'], data.keys())

    def test_cod_imovel_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['cod_imovel'], self.imovel_attributes['cod_imovel'])

    def test_limite_hospedes_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['limite_hospedes'], self.imovel_attributes['limite_hospedes'])

    def test_aceita_animais_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['aceita_animais'], self.imovel_attributes['aceita_animais'])

    def test_valor_limpeza_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['valor_limpeza'], "{:2.f}".format(self.imovel_attributes['valor_limpeza']))

    def test_validation(self):
        data = self.imovel_attributes
        data['limite_hospedes'] = -1  # Limite de hospedes não pode ser negativo
        serializer = ImovelSerializer(data=data)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
