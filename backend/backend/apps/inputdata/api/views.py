# Modules
from backend.modules.core.viewsets import ModelViewSet

# Apps
from backend.apps.inputdata.api.serializers import InputDataSerializer, SummonerDataSerializer
from backend.apps.inputdata.models import InputData, SummonerData

# Main Section
class InputDataViewSet(ModelViewSet):
    serializer_class = InputDataSerializer
    queryset = InputData.objects.all()


class SummonerDataViewSet(ModelViewSet):
    serializer_class = SummonerDataSerializer
    queryset = SummonerData.objects.all()
