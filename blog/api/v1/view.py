from rest_framework import generics , status
from rest_framework.response import Response
from .serializer import UserSerializer , serializerTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
class reqistration(generics.GenericAPIView):
    serializer_class =UserSerializer

    def post(self, request, *args, **kwargs):
        serializer= UserSerializer(data= request.data)
        if serializer.is_valid():
            data = {
                'username':serializer.validated_data['username']
            }
            serializer.save()
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class customTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializerTokenObtainPairView
    pass
