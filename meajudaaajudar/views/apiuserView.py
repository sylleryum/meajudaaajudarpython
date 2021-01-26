from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from meajudaaajudar.models import ApiUser
from meajudaaajudar.serializers import ApiUserSerializer


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
def apiuser_list(request):
    apiuser = ApiUser.objects.all()
    print('===get estados===')
    print(apiuser)
    serializer = ApiUserSerializer(apiuser, context={'request': request}, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def apiuser_detail(request, pk):
    apiuser = ApiUser.objects.get(pk=pk)
    serializer = ApiUserSerializer(apiuser, context={'request': request})
    return Response(serializer.data)
