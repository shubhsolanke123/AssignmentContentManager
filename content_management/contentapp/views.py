from django.shortcuts import render
from .permission import IsAuthororAdmin
# Create your views here.
from .models import Content
from .serializers import ContentSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication


class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Content.objects.all()
    serializer_class=ContentSerializer
    authentication_classes=[TokenAuthentication,]
    permission_classes=[IsAuthororAdmin]


    