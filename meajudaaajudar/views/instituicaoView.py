from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from meajudaaajudar.models import Instituicao
from meajudaaajudar.serializers import InstituicaoSerializer


# class CidadeView(APIView):
#
#     def get(self, request):
#         cidades = Cidade.objects.all()
#         print('===get cidades===')
#         print(cidades)
#         serializer = CidadeSerializer(cidades, many=True, context={'request': request})
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['get'])
def instituicoes_list(request):
    instituicoes = Instituicao.objects.all()
    print(instituicoes)
    serializer = InstituicaoSerializer(instituicoes, many=True, context={'request': request})
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def instituicoes_detail(request, pk):
    instituicoes = Instituicao.objects.get(pk=pk)
    serializer = InstituicaoSerializer(instituicoes, context={'request': request})
    return Response(serializer.data)
