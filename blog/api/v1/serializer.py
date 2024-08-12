from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
class UserSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=255)
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
