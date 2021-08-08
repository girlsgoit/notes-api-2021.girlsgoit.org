from rest_framework.decorators import api_view
from notes.serializers import note_serializer
from rest_framework.response import Response
from notes.models import Note


@api_view(['POST', 'GET'])
def notes(request):
    if request.method == 'POST':
        new_data = request.data
        new_data['user'] = request.user.id
        serializer = note_serializer.NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response()
    elif request.method == 'GET':
        note = Note.objects.all()
        serializer = note_serializer.NoteSerializer(note, many=True)
        return Response(serializer.data)
