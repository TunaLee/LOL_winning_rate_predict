# Modules
from backend.modules.core.viewsets import ModelViewSet

# Apps
from backend.apps.champs.api.serializers import ChampSerializer
from backend.apps.champs.models import Champ

# Main Section
class ChampViewSet(ModelViewSet):
    serializer_class = ChampSerializer
    queryset = Champ.objects.all()
