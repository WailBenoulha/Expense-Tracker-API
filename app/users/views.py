from rest_framework import generics
from .serializers import UserSerializer
from core.models import CustomUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny


class CreateUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

class UpdateUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class DeleteUserView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer  
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class getUserView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer 
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]        