from typing import Dict
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255,write_only=True)
    class Meta:
        model = User
        fields = ['username','password','password1']

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password1'):
            raise serializers.ValidationError('Passwords do not match.')
        try:
            validate_password(attrs.get('password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'email': list(e.messages)})
        return super().validate(attrs)
    def create(self, validated_data):
        validated_data.pop('password1')
        return User.objects.create(**validated_data)
#
class serializerTokenObtainPairView(TokenObtainPairSerializer):
    def validate(self, attrs):
        validated_data= super().validate(attrs)
        validated_data['username'] = self.user.username
        validated_data['user_id'] = self.user.id
        return validated_data
