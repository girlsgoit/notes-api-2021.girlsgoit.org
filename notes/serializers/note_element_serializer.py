from notes.models import NoteElement
from rest_framework.serializers import  ModelSerializer

class NoteElementSerializer(ModelSerializer):
    class Meta:
        model = NoteElement
        exclude = ['note']