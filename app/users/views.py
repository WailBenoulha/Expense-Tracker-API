from rest_framework import generics
from .serializers import UserSerializer
from core.models import CustomUser

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UpdateUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 

class DeleteUserView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer  

class getUserView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer         