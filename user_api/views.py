from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from user_api.models import User
from user_api.serializer import UserSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def user_all(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_serialized = UserSerializer(users, many=True)
        return Response(user_serialized.data)

    elif request.method == 'POST':
        user_serialized = UserSerializer(data=request.data)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(user_serialized.data, status=status.HTTP_201_CREATED)
        return Response(user_serialized.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def user_id(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        user_serialized = UserSerializer(user)
        return Response(user_serialized.data)
    
    elif request.method == 'PUT':
        user_serialized = UserSerializer(user, data=request.data, partial=True)
        if user_serialized.is_valid():
            user_serialized.save()
            return Response(user_serialized.data)
        return Response(user_serialized.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
