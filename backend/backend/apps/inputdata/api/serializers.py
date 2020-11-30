from rest_framework import serializers


# Local
from backend.modules.core.serializers import ModelSerializer
from ..models import InputData ,SummonerData

class InputDataSerializer(ModelSerializer):
    class Meta:
        model = InputData
        fields = '__all__'


class SummonerDataSerializer(ModelSerializer):
    class Meta:
        model = SummonerData
        fields = '__all__'

