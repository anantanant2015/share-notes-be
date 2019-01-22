from django.urls import path
from .views import (
	NoteListView,
	NoteDetailView,
	NoteCreateView,
	NoteUpdateView,
	NoteDeleteView,
	UserListView,
	UserDetailView,
	UserCreateView,
	UserUpdateView,
	UserDeleteView,
	UserNoteListView,
	UserNoteDetailView,
	UserNoteCreateView,
	UserNoteUpdateView,
	UserNoteDeleteView
)

urlpatterns = [
	path('note/', NoteListView.as_view()),
	path('note-create/', NoteCreateView.as_view()),
	path('note/<pk>', NoteDetailView.as_view()),
	path('note/<pk>/update/', NoteUpdateView.as_view()),
	path('note/<pk>/delete/', NoteDeleteView.as_view()),
	path('user/', UserListView.as_view()),
	path('user-create/', UserCreateView.as_view()),
	path('user/<pk>', UserDetailView.as_view()),
	path('user/<pk>/update/', UserUpdateView.as_view()),
	path('user/<pk>/delete/', UserDeleteView.as_view()),
	path('usernote/', UserNoteListView.as_view()),
	path('usernote-create/', UserNoteCreateView.as_view()),
	path('usernote/<pk>', UserNoteDetailView.as_view()),
	path('usernote/<pk>/update/', UserNoteUpdateView.as_view()),
	path('usernote/<pk>/delete/', UserNoteDeleteView.as_view())
]