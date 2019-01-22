from rest_framework.generics import ListAPIView, RetrieveAPIView
from sharenotes.models import Note, User, UserNote
from .serializers import NoteSerializer, UserSerializer, UserNoteSerializer


class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class NoteDetailView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserNoteListView(ListAPIView):
    queryset = UserNote.objects.all()
    serializer_class = UserNoteSerializer


class UserNoteDetailView(RetrieveAPIView):
    queryset = UserNote.objects.all()
    serializer_class = UserNoteSerializer

