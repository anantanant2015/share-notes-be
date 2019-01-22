from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.description


class User(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class UserNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)

