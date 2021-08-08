from rest_framework.decorators import api_view
from notes.serializers import NoteSerializer


@api_view(['POST'])
def post_note(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
