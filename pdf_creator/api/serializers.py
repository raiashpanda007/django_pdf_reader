from rest_framework import serializers
from django.contrib.auth.models import get_user_model
from .models import CustomUser



class Signup(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(max_length=255, required=True)
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }
    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)