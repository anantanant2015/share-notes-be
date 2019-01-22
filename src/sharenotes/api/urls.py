from django.urls import path
from .views import NoteListView, NoteDetailView, UserListView, UserDetailView, UserNoteListView, UserNoteDetailView

urlpatterns = [
	path('', NoteListView.as_view()),
	path('<pk>', NoteDetailView.as_view()),
    path('', UserListView.as_view()),
	path('<pk>', UserDetailView.as_view()),
    path('', UserNoteListView.as_view()),
	path('<pk>', UserNoteDetailView.as_view())
]