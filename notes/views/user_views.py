from rest_framework.decorators import api_view
from rest_framework.response import Response
from notes.serializers import user_serializer


@api_view(["POST"])

# Create your views here.
def register(request):
    if request.method == "POST":
       print(request.data)
       serializer = user_serializer.UserSerializer(data = request.data)
       if serializer.is_valid():
          serializer.save()
       return Response()