from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from .models import Reservas
from .serializers import ReservaSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class ReservaViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Reservas.objects.all()
    serializer_class = ReservaSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        raise ValidationError("Não é permitido alterar uma reserva.")

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.full_clean()
        instance.save()