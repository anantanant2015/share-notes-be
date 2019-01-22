from rest_framework import viewsets
from sharenotes.models import Note, User, UserNote
from .serializers import NoteSerializer, UserSerializer, UserNoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserNoteViewSet(viewsets.ModelViewSet):
    serializer_class = UserNoteSerializer
    queryset = UserNote.objects.all()

