from rest_framework import serializers


# Local
from backend.modules.core.serializers import ModelSerializer
from ..models import InputData

class InputDataSerializer(ModelSerializer):
    class Meta:
        model = InputData
        fields = '__all__'


