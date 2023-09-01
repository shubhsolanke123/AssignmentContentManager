from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import UserSerializer

class UserRegisterApi(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer

class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer    
    