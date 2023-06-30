from rest_framework import serializers
from .models import Reservas

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'
