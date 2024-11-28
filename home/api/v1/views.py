from rest_framework import mixins , viewsets ,generics
from django.shortcuts import render ,HttpResponse ,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializer import Productserializer , commentserializer ,Categoryserializer ,OrderSerializer ,contactSerializer ,contactcreatSerializer ,adressSerializer ,CartSerializer , addCartSerializer ,profileSerializer
from ...models import product ,Category , Order , comment ,contact ,CustomUser , adresses
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


class cartApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return addCartSerializer
        return CartSerializer
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

        if deleteStatus:
            return Response({
                'message': 'Item deleted successfully',
                'item_id': pk  
            }, status=204)
        else:
            return Response({
                'message': 'The item could not be deleted. There is a problem',
                'item_id': pk
            }, status=400)
    def create(self, request  , *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart =Cart(request)
        pk = int (request.data.get('id'))


        cart.add(pk)

        return Response({
            'message': 'Item added successfully',
            'item_id': pk
        },status=201)

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
    queryset = comment.objects.filter(status=True)
    filter_backends = [OrderingFilter]
    ordering_fields = ['created_date']


class profileViewSet(viewsets.ModelViewSet):
    pagination_class = [IsAuthenticated]
    serializer_class =profileSerializer
    pagination_class = Resultpagniton
    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

class CategorysApiView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = Categoryserializer
    queryset = Category.objects.all()

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class=OrderSerializer
    pagination_class = Resultpagniton

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.id)


class favoratesViewSet(generics.ListAPIView):
    serializer_class = Productserializer


    def get_queryset(self):
        user = self.request.user
        return user.favorites.all()

class favoratesCreateViewSet(generics.CreateAPIView):
    serializer_class = addCartSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        p=get_object_or_404(product,pk=request.POST.get('id'))
        request.user.favorites.add(p)
        return Response({
            'message' : 'product added'
        })




class listticketViewSet(viewsets.ModelViewSet):
    # queryset = contact.objects.all()
    serializer_class = contactSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Resultpagniton
    ordering_fields = ['created_date']

    def get_queryset(self):
        return contact.objects.filter(name=self.request.user)

class AdressView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    pagination_class = Resultpagniton
    serializer_class= adressSerializer
    def get_queryset(self):
        return adresses.objects.filter(user=self.request.user)


class addadressApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
         data =request.data.copy()
         serializer = adressSerializer(data=data)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED )
         return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class CatApiView(APIView):
    def get(self,request,cat_name):
        products = product.objects.filter(category__name = cat_name)
        res = Productserializer(products , many=True)
        return Response({
            'data' : res.data
        })

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
