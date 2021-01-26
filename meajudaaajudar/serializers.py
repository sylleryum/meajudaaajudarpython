from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, HyperlinkedModelSerializer
from meajudaaajudar.models import Estado, Cidade, ApiUser, Instituicao


class CidadeSerializer(HyperlinkedModelSerializer):
    estado = serializers.SlugRelatedField(queryset=Estado.objects.all(),
                                          slug_field='nome')
    url = HyperlinkedIdentityField(
        read_only=True,
        view_name='cidades-detail', )

    class Meta:
        model = Cidade
        fields = ('nome', 'estado', 'url')
        depth = 2


class EstadoSerializer(HyperlinkedModelSerializer):
    cidade = CidadeSerializer(many=True, read_only=True)
    url = HyperlinkedIdentityField(
        read_only=True,
        view_name='estados-detail')

    class Meta:
        model = Estado
        fields = ('nome', 'cidade', 'url')


class InstituicaoSerializer(HyperlinkedModelSerializer):
    cidade = CidadeSerializer()
    self = HyperlinkedIdentityField(
        read_only=True,
        view_name='instituicoes-detail')

    class Meta:
        model = Instituicao
        fields = ('id', 'nome', 'cidade', 'imagem', 'descricao', 'doar_link', 'sobre', 'url', 'info_doacao', 'self')











#######################
class ApiUserSerializer(HyperlinkedModelSerializer):
    url = HyperlinkedIdentityField(view_name='apiuser-list')

    class Meta:
        model = ApiUser
        fields = ('url', 'username')
