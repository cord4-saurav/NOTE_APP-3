from rest_framework import serializers
from .models import NoteAPI

class Note_APISerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteAPI
        fields = ['NoteID', 'subject', 'description']