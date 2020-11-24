# Modules
from backend.modules.core.viewsets import ModelViewSet

# Apps
from backend.apps.inputdata.api.serializers import InputDataSerializer
from backend.apps.inputdata.models import InputData

# Main Section
class InputDataViewSet(ModelViewSet):
    serializer_class = InputDataSerializer
    queryset = InputData.objects.all()
