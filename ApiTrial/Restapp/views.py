from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from Restapp.serializers import UserCreationserializer,Bookserializer,Loginserializer
from rest_framework.response import Response
from rest_framework import status
from Restapp.models import Book
from django.http import Http404
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login as djangologin,logout as djangologout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


# Create your views here.

class Userview(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer=UserCreationserializer(user,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserCreationserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class Books(APIView):
    authentication_classes = (TokenAuthentication,)
    def get(self,request):
        books=Book.objects.all()
        serializer=Bookserializer(books,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)




class BookDetail(APIView):
    authentication_classes = [SessionAuthentication,BasicAuthentication]
    permission_classes = [IsAuthenticated]
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = Bookserializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = Bookserializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    
    def post(self,request):
        serializer = Loginserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer._validated_data['user']
        djangologin(request,user)
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key},status=200)

from rest_framework.authentication import TokenAuthentication
class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self,request):
        djangologout(request)
        print("logout")
        return Response(status=204)
        

