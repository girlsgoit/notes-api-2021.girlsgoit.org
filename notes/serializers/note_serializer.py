from rest_framework.serializers import ModelSerializer
from note_element_serializer import NoteElementSerializer
from ..models import Note, NoteElement


class NoteSerializer(ModelSerializer):
    note_elements = NoteElementSerializer(many=True)
    class Meta:
        model = Note
        fields = '__all__'

    def create(self, validated_data):
        note_elements = validated_data.pop('note_elements')
        note = Note.objects.create(**validated_data)
        for note_element in note_elements:
            NoteElement.objects.create(note=note, tag=note_element["tag"], content=note_element["content"])
        return note
        
    def update(self, instance, validated_data):
        instance.note_element.all().delete
        note_elements = validated_data.pop('note_elements')
        for note_element in note_elements:
            NoteElement.objects.create(note=instance, tag=note_element["tag"], content=note_element["content"])
        return instance 