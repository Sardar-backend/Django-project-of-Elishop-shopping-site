from rest_framework import generics , status
from rest_framework.response import Response
from .serializer import UserSerializer
class reqistration(generics.GenericAPIView):
    serializer_class =UserSerializer

    def post(self, request, *args, **kwargs):
        serializer= UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'username':serializer.validated_data['username']
            }
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
