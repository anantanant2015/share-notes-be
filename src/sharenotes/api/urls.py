from sharenotes.api.views import NoteViewSet, UserViewSet, UserNoteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'note', NoteViewSet, base_name='note')
router.register(r'user', UserViewSet, base_name='user')
router.register(r'usernote', UserNoteViewSet, base_name='usernote')
urlpatterns = router.urls