from rest_framework import serializers
from .models import Content,UserDetails




class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Content
        fields= '__all__'

class userialiserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        fields= '__all__'

