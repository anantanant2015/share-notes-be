from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    CreateAPIView,
	UpdateAPIView,
	DestroyAPIView
)
from sharenotes.models import Note, User, UserNote
from .serializers import NoteSerializer, UserSerializer, UserNoteSerializer


class NoteListView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteCreateView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteUpdateView(UpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDeleteView(DestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserNoteListView(ListAPIView):
    queryset = UserNote.objects.all()
    serializer_class = UserNoteSerializer


class UserNoteDetailView(RetrieveAPIView):
    queryset = UserNote.objects.all()
    serializer_class = UserNoteSerializer

class UserNoteCreateView(CreateAPIView):
    queryset = UserNote.objects.all()
    serializer_class = UserNoteSerializer

class UserNoteUpdateView(UpdateAPIView):
    queryset = UserNote.objects.all()
    serializer_class = UserNoteSerializer

class UserNoteDeleteView(DestroyAPIView):
    queryset = UserNote.objects.all()
    serializer_class = UserNoteSerializer