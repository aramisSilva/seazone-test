from rest_framework import serializers
from .models import Imovel

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = ['id', 'cod_imovel', 'limite_hospedes', 'qtd_banheiros', 'aceita_animais', 'valor_limpeza', 'data_ativacao',
                  'data_criacao', 'data_atualizacao']