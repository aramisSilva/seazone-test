from django.core.management.base import BaseCommand
from reservas.models import Reservas
from anuncios.models import Anuncios
import random
import datetime

class Command(BaseCommand):
    help = "Cria reservas aleatórias para teste"

    def handle(self, *args, **options):
        Reservas.objects.all().delete()
        anuncios = Anuncios.objects.all()

        for i in range(8):
            anuncio = random.choice(anuncios)
            check_in = datetime.date.today() + datetime.timedelta(days=random.randint(1, 10))
            check_out = check_in + datetime.timedelta(days=random.randint(1, 10))
            Reservas.objects.create(
                codigo_reserva = 'RES' + str(i+1),
                anuncio = anuncio,
                check_in = check_in,
                check_out = check_out,
                preco_total = random.randint(100, 500),
                comentario = 'Comentário ' + str(i+1),
                numero_hospedes = random.randint(1, 5),
            )

        self.stdout.write(self.style.SUCCESS('8 reservas criadas com sucesso!'))
