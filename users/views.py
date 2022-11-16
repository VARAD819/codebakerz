import PIL
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class RegisterUser(APIView):
    #create user&profile
    def post(self, request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'errors':serializer.errors})

        serializer.save()
        return Response(serializer.data)


class Profiles(APIView):
    # display all profiles
    def get(self, request):
        profile_set = User.objects.all()
        serializer = ProfileSerializer(profile_set, many=True)
        return Response(serializer.data)


class Profile(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({
                'message':'User does not exist or Invalud ID'
            })
    
    # display particular profile i.e. Read
    def get(self, request, pk):
        profile = self.get_object(pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    # update profile
    def patch(self, request, pk):
        profile = self.get_object(pk)
        data = request.data
        serializer = ProfileSerializer(profile, data=data, partial=True)
        
        if not serializer.is_valid():
            return Response({
                'error':serializer.errors
            })

        serializer.save()
        return Response({
            'payload':serializer.data,   
            'message':'User Updated'
        })

    #delete profile
    def delete(self, request, pk):
        try:
            profile = self.get_object(pk)
            profile.delete()
            return Response({
                'Profile Deleted Successfully'
            })
        except Exception as e:
            {
                'message':'Invalid ID'
            }