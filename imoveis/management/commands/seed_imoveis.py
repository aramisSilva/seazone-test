import random
from django.core.management.base import BaseCommand
from imoveis.models import Imovel

class Command(BaseCommand):
    help = "Cria dados iniciais para a tabela Imóvel"

    def handle(self, *args, **options):
        Imovel.objects.all().delete() #remove instâncias existentes no DB
        for i in range(5):
            Imovel.objects.create(
                cod_imovel=f'cod_{i}',
                limite_hospedes=i + 1,
                qtd_banheiros=i + 1,
                aceita_animais=True,
                valor_limpeza=150.0,
                data_ativacao=None
            )
        self.stdout.write(self.style.SUCCESS('5 imóveis foram criados com sucesso!'))