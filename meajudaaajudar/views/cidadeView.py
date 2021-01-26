from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from meajudaaajudar.models import Cidade
from meajudaaajudar.serializers import CidadeSerializer


# class CidadeView(APIView):
#
#     def get(self, request):
#         cidades = Cidade.objects.all()
#         print('===get cidades===')
#         print(cidades)
#         serializer = CidadeSerializer(cidades, many=True, context={'request': request})
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['get'])
def cidades_list(request):
    cidades = Cidade.objects.all()
    print('===get cidades===')
    print(cidades)
    serializer = CidadeSerializer(cidades, many=True, context={'request': request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def cidades_detail(request, pk):
    cidade = Cidade.objects.get(pk=pk)
    serializer = CidadeSerializer(cidade, context={'request': request})
    return Response(serializer.data)
