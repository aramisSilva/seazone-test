import uuid
from django.db import models
from anuncios.models import Anuncios
from django.core.exceptions import ValidationError


class Reservas(models.Model):
    codigo_reserva = models.CharField(max_length=200, default=uuid.uuid4, unique=True)
    anuncio = models.ForeignKey(Anuncios, on_delete=models.CASCADE, related_name='reservas')
    check_in = models.DateField()
    check_out = models.DateField()
    preco_total = models.FloatField()
    comentario = models.TextField(null=True, blank=True)
    numero_hospedes = models.PositiveIntegerField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()  # chama a validação padrão primeiro

        if self.check_in >= self.check_out:
            raise ValidationError("A data de check-in não pode ser posterior ou igual à data de check-out.")