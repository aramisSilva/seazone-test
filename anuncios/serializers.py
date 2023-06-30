from rest_framework import serializers
from .models import Anuncios


class AnunciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncios
        fields = ['id', 'imovel', 'nome_plataforma', 'taxa_plataforma', 'data_criacao', 'data_atualizacao']
