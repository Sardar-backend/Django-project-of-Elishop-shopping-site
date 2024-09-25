from rest_framework import mixins , viewsets
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import Productserializer , commentserializer ,Categoryserializer ,OrderSerializer ,contactSerializer
from ...models import product ,Category , Order , comment ,contact
from rest_framework.filters import OrderingFilter
from .paginiton import Resultpagniton
from rest_framework.permissions import IsAuthenticated
# Create your views here.
# @api_view()
# def api_view(request):
#     return Response('ok')
class ProductApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Productserializer
    queryset = product.objects.filter(status=True)
    filter_backends = [OrderingFilter]
    ordering_fields = ['updated_date']
    pagination_class = Resultpagniton
class CommentViewSetApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = commentserializer
    # queryset = comment.objects.filter(status=True)
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_date']
    def get_queryset(self):
        id = self.kwargs.get('id')
        return comment.objects.filter(pro_id= id, status=True)
    # pagination_class = Resultpagniton

class CategorysApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Categoryserializer
    queryset = Category.objects.all()
    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['pro'] = Productserializer(instance.pro)
    #     return rep
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class=OrderSerializer
    pagination_class = Resultpagniton

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.id)


class favoratesViewSet(viewsets.ModelViewSet):
    # permission_classes =[IsAuthenticatedOrReadOnly]
    # serializer_class=OrderSerializer
    # pagination_class = Resultpagniton

    # def get_queryset(self):
    #     return Order.objects.filter(user=self.request.user.id)
    serializer_class = Productserializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.favorites.all()

class listticketViewSet(viewsets.ModelViewSet):
    # permission_classes =[IsAuthenticatedOrReadOnly]
    # serializer_class=OrderSerializer
    # pagination_class = Resultpagniton

    # def get_queryset(self):
    #     return Order.objects.filter(user=self.request.user.id)
    serializer_class = contactSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Resultpagniton
    ordering_fields = ['created_date']

    def get_queryset(self):
        return contact.objects.filter(name=self.request.user)
