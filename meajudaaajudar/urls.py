"""meajudaaajudarpython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from meajudaaajudar.views.cidadeView import cidades_list, cidades_detail
from meajudaaajudar.views.estadoView import estados_list, estados_detail
from meajudaaajudar.views.instituicaoView import instituicoes_list, instituicoes_detail
from meajudaaajudar.views.apiuserView import apiuser_list, apiuser_detail


# router = routers.DefaultRouter()
# router.register("cidades", CidadeView, '')
urlpatterns = [
    path('estados/', estados_list),
    path('estados/<int:pk>', estados_detail, name="estados-detail"),

    path('cidades/', cidades_list),
    path('cidades/<int:pk>', cidades_detail, name="cidades-detail"),

    path('instituicoes/', instituicoes_list),
    path('instituicoes/<int:pk>', instituicoes_detail, name="instituicoes-detail"),


    path('apiuser/', apiuser_list, name="apiuser-list"),
    path('apiuser/<int:pk>', apiuser_detail),
]
