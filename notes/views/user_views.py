from rest_framework.decorators import api_view
from rest_framework.response import Response
from notes.serializers import user_serializer
from notes.models import GGITUser


@api_view(["POST"])
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
