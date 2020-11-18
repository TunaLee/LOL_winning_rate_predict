# Local
from ..models import Champ,ChampRole
from masuter_backend.modules.core.serializers import ModelSerializer

class ChampSerializer(ModelSerializer):
    class Meta:
        model = Champ
        fields = '__all__'


class ChampRoleSerializer(ModelSerializer):
    cham = ChampSerializer(read_only=True)
    class Meta:
        model = ChampRole
        fields = '__all__'






