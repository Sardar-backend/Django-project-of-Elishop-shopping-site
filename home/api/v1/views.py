from rest_framework import mixins , viewsets
from django.shortcuts import render ,HttpResponse ,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import Productserializer , commentserializer ,Categoryserializer ,OrderSerializer ,contactSerializer ,contactcreatSerializer ,adressSerializer ,CartSerializer
from ...models import product ,Category , Order , comment ,contact
from rest_framework.filters import OrderingFilter
from .paginiton import Resultpagniton
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from blog.cart import Cart
from rest_framework.exceptions import NotFound
# Create your views here.
# @api_view()
# def api_view(request):
#     return Response('ok')
class indexApiView(APIView):
    def get(self, request, format=None):
        mobile_products =product.objects.filter(category__name="موبایل گوشی",status=True).order_by('updated_date')[:10]
        mobile_products_serializer  =Productserializer(mobile_products , many =True)

        Phone_equipment_products =product.objects.filter(category__name="تجهیزات جانبی گوشی",status=True).order_by('updated_date')[:10]
        Phone_equipment_serializer  =Productserializer(Phone_equipment_products , many =True)

        headphones_products =product.objects.filter(category__name="هدفون، هدست و هندزفری",status=True).order_by('updated_date')[:10]
        headphones_serializer  =Productserializer(headphones_products , many =True)

        most_viewed_products = product.objects.filter(counted_view__gt = 200).order_by('counted_view')[:10]
        most_viewed_products_serializer = Productserializer(most_viewed_products , many=True)
        return Response({
            'mobile_products' : mobile_products_serializer.data,
            'most_viewed_products' : most_viewed_products_serializer.data,
            'Phone_equipment_products' : Phone_equipment_serializer.data,
            'headphones_products' : headphones_serializer.data


        })

# class cartApiView(APIView):
#     def get(self, request):
#         cart_items = Cart(request)
#         serializer = CartSerializer(cart_items, many=True)
#         return Response(serializer.data)
#         # x = Cart(request)
#         # return HttpResponse( x)
#     def delete(self, request ,product_id):
#         pro =get_object_or_404(product ,id = product_id)
#         Cart.remove(pro)
#         return Response({
#             'massage' : 'deleted successfully'
#         })
#     def post (self, request, product_id):
#         pro =get_object_or_404(product ,id = product_id)
#         Cart.add(pro)
#         return Response({
#             'massage' : 'add successfully'
#         })

class cartApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CartSerializer
    def get_queryset(self):
        return Cart(self.request)
    def retrieve(self, request, pk=None):
        cart_items = self.get_queryset()
        item = next((item for item in cart_items if item['id'] == pk), None)
        if item is None:
            raise NotFound(detail="Item not found", code=404)
        serializer = self.get_serializer(item)
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        cart=Cart(request)
        deleteStatus=cart.remove(pk)
        # return HttpResponse(b)
        if deleteStatus:
            return Response({
                'message': 'Item deleted successfully',
                'item_id': pk  # می‌توانید شناسه کالا را هم برگردانید
            }, status=204)
        else:
            return Response({
                'message': 'The item could not be deleted. There is a problem',
                'item_id': pk  # می‌توانید شناسه کالا را هم برگردانید
            }, status=400)

    # def destroy(self, request, pk=None):
    #     cart_items = self.get_queryset()
    #     item = next((item for item in cart_items if item['id'] == pk),None)
    #     if item is None:
    #         raise NotFound(detail="Item not found", code=404)
    #     cart = self.get_queryset()
    #     p =product.objects.get(pk=pk)
    #     cart.remove(p)
    #     return Response({
    #         'message':'Item deleted successfully',
    #     },status=204)
class ProductApiView(viewsets.ReadOnlyModelViewSet):
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

class CategorysApiView(viewsets.ReadOnlyModelViewSet):
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
    queryset = contact.objects.all()
    serializer_class = contactSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Resultpagniton
    ordering_fields = ['created_date']

    def get_queryset(self):
        return contact.objects.filter(name=self.request.user)

class addadressApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
         data =request.data.copy()
         serializer = adressSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED )
         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


# class TicketCreateView(APIView):
#     permission_classes =[IsAuthenticated]

#     def post(self,request):
#         data =request.data.copy()
#         # return HttpResponse( request.data)
#         # data['name'] = request.user.id
#         #         # data['content'] = request.data
#         # # return HttpResponse(request.data)
#         # data['content'] = str (data)
#         serializer = contactcreatSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED )
#         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
