from notes.models import GGITUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from notes.serializers import user_serializer
from django.shortcuts import get_object_or_404

@api_view(["GET"])
@permission_classes(['IsAuthenticated'])
def user_detail(request,user_id):
   user = get_object_or_404(GGITUser, pk=user_id)
   if request.method == "GET":
      serialized_user = UserSerializer(user)
      return Response(serialized_user.data)


def register(request):
    if request.method == "POST":
        print(request.data)
        serializer = user_serializer.UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()


@api_view(["POST"])
def is_unique(request):
    if request.method == "POST":
        print(request.data)
        if GGITUser.objects.filter(username=request.data['username']).exists():
            return Response(status = 400)
        else:  
            return Response(status = 200)

@api_view(['GET'])
@permission_classes(['IsAuthenticated'])
def user_me(request):
    user_data = request.user
    serialised_user_me = user_serializer.UserSerializer(user_data)
    return Response(serialised_user_me.data)
