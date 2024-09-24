from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

#user login 
class LoginUser(APIView):
    def post(self,request):
      data=request.data
      serializer=LoginSerializer(data=data)
      if not serializer.is_valid():
          return Response({
              'stauts':False,
              'message': serializer.errors
          }, status.HTTP_400_BAD_REQUEST)
      user=authenticate(username=serializer.data['username'],password=serializer.data['password'])
      print(serializer.data)
      print(user)
      if not user:
           return Response({
              'stauts':False,
              'message':'invalid credentials'
          }, status.HTTP_400_BAD_REQUEST)
          
      token, created = Token.objects.get_or_create(user=user)
      print(token)
      return Response({'status':True,'message':'userlogined', 'token':str(token)},status.HTTP_200_OK)
    
# registeruser
class registerUser(APIView):
    def post(self,request):
      data=request.data
      serializer=registerserializer(data=data)
      if not serializer.is_valid():
          return Response({
              'status':False,
              'message': serializer.errors
          }, status.HTTP_400_BAD_REQUEST)
      serializer.save()
      return Response({'status':True,'message':'user created'},status.HTTP_200_OK)
    
# access members
# "token": "42be20f4c097e0e7204229029f6c668fcda33dbe"  { "username": "sri", "email": "sri@gmail.com", "password":  "sri@123"}
class MymemberView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        member = MyModel.objects.all()
        serializer = MyModelSerializer(member, many=True)
        return render(request,'myapp/home.html',{'last':serializer.data})
 
    def post(self, request):
        serializer = MyModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        member = MyModel.objects.get(pk=pk)
        serializer = MyModelSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # we want to give all data to update the data with id.
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        member = MyModel.objects.get(pk=pk)
        serializer=MyModelSerializer(member,data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            # we want to give that change characteristic only with id.
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        member = MyModel.objects.get(pk=pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


