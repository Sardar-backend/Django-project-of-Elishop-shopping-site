from rest_framework import generics , status
from rest_framework.response import Response
from .serializer import UserSerializer , serializerTokenObtainPairView , changePasswordView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.core.mail import send_mail
from django.contrib.auth.models import User
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
class changepasswordView(generics.UpdateAPIView):

    model = User
    # permission_classes = [IsAuthenticated]
    serializer_class = changePasswordView

    def get_object(self,queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data =request.data)
        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({'error': 'Old password is wrong.'}, status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail': 'Password has been changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class send_email(generics.GenericAPIView):
    
    def get(self, request, *args, **kwargs):
        send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        ["to@example.com"],
        fail_silently=False,
        )
        return Response('success', status=status.HTTP_200_OK)
