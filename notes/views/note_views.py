from rest_framework.decorators import api_view
from notes.serializers import note_serializer
from rest_framework.response import Response


@api_view(['POST'])
def post_note(request):
    serializer = note_serializer.NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response()


@api_view(['GET'])
@permission_classes(['IsAuthenticated'])
def note_details(request,note_id):
    note=get_object_or_404(Note,pk=note_id)
    serialized_note=NoteSerializer(note)
    if request.method == "GET":
        return Response(serialised_note.data)
