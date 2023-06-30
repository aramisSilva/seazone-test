from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Imovel
from .serializers import ImovelSerializer

class ImovelViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Imovel.objects.all()
    serializer_class = ImovelSerializer