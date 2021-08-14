from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from notes.serializers import note_element_serializer, note_serializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from notes.models import Note
from drf_yasg import openapi


@swagger_auto_schema(
    method='get', operation_description="Get the list of notes.",
    responses={200: note_serializer.NoteSerializer()},
)
# @swagger_auto_schema(
#     method='post', operation_description="Create a new note.",
#     request_body=note_serializer.NoteSerializer(), responses={201: note_serializer.NoteSerializer()},
# )
@swagger_auto_schema(
    method='post', operation_description="Create a new note",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "note_elements":  openapi.Schema(type=openapi.TYPE_OBJECT,
                                             properties={
                                                 "tag":  openapi.Schema(type=openapi.TYPE_STRING, description='tag'),
                                                 "content":  openapi.Schema(type=openapi.TYPE_STRING, description='content')
                                             }, required=["tag", "content"])
        },
        required=["note_elements"]
    ),
    responses={201: note_serializer.NoteSerializer()},
)
@api_view(['POST', 'GET'])
def notes(request):
    if request.method == 'POST':
        new_data = request.data
        new_data['user'] = request.user.id
        serializer = note_serializer.NoteSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        note = Note.objects.all()
        serializer = note_serializer.NoteSerializer(note, many=True)
        return Response(serializer.data)


@swagger_auto_schema(
    method='get', operation_description="Get an individual note.",
    responses={200: note_serializer.NoteSerializer()},
)
@swagger_auto_schema(
    method='delete', operation_description="Delete a note",
    responses={200: {}},
)
@swagger_auto_schema(
    method='put', operation_description="Update note.",
    responses={200: note_serializer.NoteSerializer()},
)
@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes(['IsAuthenticated'])
def note_details(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    serialized_note = note_serializer.NoteSerializer(note)
    if request.method == "GET":
        return Response(serialized_note.data)
    elif request.method == 'PUT':
        request_data = request.data
        request_data['user'] = request.user.id
        serialized_note = note_serializer.NoteSerializer(note, request_data)
        if serialized_note.is_valid():
            serialized_note.save()
            return Response(serialized_note.data)
        else:
            return Response(serialized_note.errors)
    else:
        note.delete()
        return Response(status=200)
