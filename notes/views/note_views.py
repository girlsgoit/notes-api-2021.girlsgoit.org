from django.shortcuts import get_object_or_404
from notes.models import GGITUser
from notes.serializers import note_serializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from notes.serializers.note_serializer import NoteSerializer



@api_view(['GET'])
@permission_classes(['IsAuthenticated'])
def note_details(request,note_id):
    note=get_object_or_404(Note,pk=note_id)
    serialized_note=NoteSerializer(note)
    if request.method == "GET":
        return Response(serialised_note.data)
    
