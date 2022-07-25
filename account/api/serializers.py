from rest_framework import serializers
from account.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
        ]
        

class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'} , write_only= True)

    class Meta:
        model = User
        fields = ('email','first_name','last_name','username','password','password2')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = User(
            email = self.validated_data['email'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            username = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords must macth.'})
        user.set_password(password)
        user.save()
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        serializer = UserSerializer(user)
        data.update(serializer.data)
        return data 

