from rest_framework import viewsets
from rest_framework.exceptions import NotAcceptable
from rest_framework.permissions import AllowAny
from .models import Anuncios
from .serializers import AnunciosSerializer

class AnuncioViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Anuncios.objects.all()
    serializer_class = AnunciosSerializer

    def destroy(self, request, *args, **kwargs):
        raise NotAcceptable('Não é possível excluir um anúncio')