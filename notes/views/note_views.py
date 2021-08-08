from rest_framework.decorators import api_view
from notes.serializers import note_serializer
from rest_framework.response import Response


@api_view(['POST'])
def post_note(request):
    serializer = note_serializer.NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()
