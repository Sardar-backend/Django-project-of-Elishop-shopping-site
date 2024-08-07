from rest_framework import mixins , viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import Postserializer , commentserializer
from ...models import product
from rest_framework.filters import OrderingFilter
from .paginiton import Resultpagniton
# Create your views here.
# @api_view()
# def api_view(request):
#     return Response('ok')
class PostApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Postserializer
    queryset = product.objects.filter(status=True)
    filter_backends = [OrderingFilter]
    ordering_fields = ['id']
    pagination_class = Resultpagniton

class commentApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = commentserializer
    queryset = product.objects.all()
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['pro'] = Postserializer(instance.pro)
    #     return rep
