import uuid
from django.db import models
from django.utils import timezone

class Imovel(models.Model):
    #se esse código for gerado automaticamente, a linha abaixo é uma boa prática.
    #cod_imovel = models.CharField(max_length=10, default=lambda: str(uuid.uuid4), editable=False, unique=True)
    cod_imovel = models.CharField(max_length=200, unique=True, default=None, blank=False, null=False)
    limite_hospedes = models.PositiveIntegerField()
    qtd_banheiros = models.PositiveIntegerField()
    aceita_animais = models.BooleanField(default=False)
    valor_limpeza = models.DecimalField(max_digits=6, decimal_places=2)
    data_ativacao = models.DateField(null=True, blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.cod_imovel

    def ativar_imovel(self):
        self.data_ativacao = timezone.now()
        self.save()