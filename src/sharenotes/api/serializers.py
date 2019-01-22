from rest_framework import serializers
from sharenotes.models import Note, User, UserNote

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'description')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class UserNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNote
        fields = ('id', 'user', 'note')