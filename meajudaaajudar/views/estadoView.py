from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from meajudaaajudar.models import Estado
from meajudaaajudar.serializers import EstadoSerializer


#
# class EstadoView(APIView):
#
#     def get(self, request):
#         estados = Estado.objects.all()
#         print('===get estados===')
#         print(estados)
#         serializer = EstadoSerializer(estados, many=True)
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['get'])
def estados_list(request):
    estados = Estado.objects.all()
    print('===get estados===')
    print(estados)
    serializer = EstadoSerializer(estados, context={'request': request}, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def estados_detail(request, pk):
    estado = Estado.objects.get(pk=pk)
    serializer = EstadoSerializer(estado, context={'request': request})
    return Response(serializer.data)
