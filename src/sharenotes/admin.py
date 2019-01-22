from django.contrib import admin
from .models import Note, User, UserNote

# Register your models here.
admin.site.register(Note)
admin.site.register(User)
admin.site.register(UserNote)