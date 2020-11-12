from django.contrib.auth.models import User
from Restapp.models import Book
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions

class UserCreationserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','last_name','email','username','password']

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields="__all__"

class Loginserializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username,password=password)
            if user:
                data['user']=user
            
            else:
                msg='unable to login given credentails'

                raise exceptions.ValidationError(msg)
        
        else:
            msg='must be provide username and password'

            raise exceptions.ValidationError(msg)
        return data
            

                



