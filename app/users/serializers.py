from rest_framework import serializers
from core import models
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ['id','email','password','first_name','last_name','profile_pic']
        extra_kwargs = {'password':{'write_only':True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)