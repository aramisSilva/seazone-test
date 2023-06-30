from django.db import models
from imoveis.models import Imovel


class Anuncios(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name='anuncios')
    nome_plataforma = models.CharField(max_length=200, default=None, blank=False, null=False)
    taxa_plataforma = models.DecimalField(max_digits=6, decimal_places=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.imovel.cod_imovel
