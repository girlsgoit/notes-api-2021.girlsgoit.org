from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from notes.models import GGITUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from notes.serializers import user_serializer
from django.shortcuts import get_object_or_404
from rest_framework import status


@api_view(["GET", "PUT"])
@permission_classes(['IsAuthenticated'])
def user_detail(request, user_id):
    user = get_object_or_404(GGITUser, pk=user_id)
    if request.method == "GET":
        serialized_user = user_serializer.UserSerializer(user)
        return Response(serialized_user.data)
    elif request.method == 'PUT':
        request_data = request.data
        serialized_user = user_serializer.UserSerializer(user, request_data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data)
        else:
            return Response(serialized_user.errors)


@swagger_auto_schema(
    method='post', operation_description="Register a user.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "username": openapi.Schema(type=openapi.TYPE_STRING, description='unique username'),
            "password": openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
            "first_name": openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
            "last_name": openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
            "email": openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
        },
        required=["username", "password"]
    ),
    responses={201: user_serializer.UserSerializer()},
)
@api_view(["POST"])
def register(request):
    password = request.data['password']
    register_serialized = user_serializer.UserSerializer(data=request.data)
    if register_serialized.is_valid():
        user_instance = register_serialized.save()
        user_instance.set_password(password)
        user_instance.save()
        return Response(register_serialized.data, status=201)
    else:
        return Response(register_serialized.errors, status=406)


@api_view(["POST"])
def is_unique(request):
    if request.method == "POST":
        print(request.data)
        if GGITUser.objects.filter(username=request.data['username']).exists():
            return Response(status=400)
        else:
            return Response(status=200)


@swagger_auto_schema(
    method='get', operation_description="Get the details of a user.",
    responses={200: user_serializer.UserSerializer()},
)
@api_view(['GET'])
@permission_classes(['IsAuthenticated'])
def user_me(request):
    user_data = request.user
    serialised_user_me = user_serializer.UserSerializer(user_data)
    return Response(serialised_user_me.data)


@api_view(['GET'])
# @permission_classes(['IsAuthenticated'])
def all_users(request):
    all_users = GGITUser.objects.all()
    serialized_all_users = user_serializer.UserSerializer(all_users, many=True)
    print(all_users)
    return Response(serialized_all_users.data)
