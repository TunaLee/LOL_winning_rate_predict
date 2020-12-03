# Modules
from backend.modules.core.viewsets import ModelViewSet
from rest_framework.views import APIView

# Apps
from backend.apps.inputdata.api.serializers import InputDataSerializer, SummonerDataSerializer
from backend.apps.inputdata.models import InputData, SummonerData
from backend.apps.inputdata.api.test import crawler
from backend.apps.inputdata.api.predict import predict, deserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Api
import pandas as pd


# Main Section
class InputDataViewSet(ModelViewSet):
    serializer_class = InputDataSerializer
    queryset = InputData.objects.all()


class SummonerDataViewSet(ModelViewSet):
    serializer_class = SummonerDataSerializer
    queryset = SummonerData.objects.all()


@api_view(['GET', 'POST'])
def SummonerView(request):

    if request.method == 'GET':
        return Response({'result':'ok'})

    if request.method == 'POST':
        # print(request.data)
        summoners = request.data

        data = deserializer(summoners)
        print(data)
        data2 = predict(data)

        return Response(data2)

@api_view(['GET'])
def SummonerByChampView(request, name):
    data = crawler(name)

    return Response(data)



# class SummonerView(APIView):
#     def get(self, request):
#         return Response({'result': 'ok'})
