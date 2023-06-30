from django.core.management.base import BaseCommand
from imoveis.models import Imovel
from anuncios.models import Anuncios
from random import choice
from datetime import datetime

class Command(BaseCommand):
    help = 'Cria dados iniciais para a tabela'

    def handle(self, *args, **options):
        imoveis = Imovel.objects.all()

        # Creating 3 anuncios
        for i in range(1, 4):
            Anuncios.objects.create(
                imovel=choice(imoveis),
                nome_plataforma=f'Plataforma {i}',
                taxa_plataforma=10*i,
                data_criacao=datetime.now(),
                data_atualizacao=datetime.now(),
            )

        self.stdout.write(self.style.SUCCESS('3 anuncios foram criados!'))
