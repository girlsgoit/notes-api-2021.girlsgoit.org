from django.contrib.auth.models import AbstractUser
from django.db import models



# User model
class GGITUser(AbstractUser):
    settings = models.TextField(blank=True, null=True)



# Note model
class Note(models.Model):
    user = models.ForeignKey(GGITUser, on_delete = models.CASCADE, related_name="notes")
    created_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.id}. Utilizator: {self.user}; Data creării: {self.created_at};"


class NoteElement(models.Model):
    tag = models.TextField()
    content = models.TextField()
    note = models.ForeignKey(Note, on_delete = models.CASCADE, related_name="note_elements")

    def __str__(self):
        return f"{self.id}. Tag: {self.tag}; {self.content}; {self.note}"
   