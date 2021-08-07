from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.db.models.fields.files import ImageFieldFile

from django.db.models.fields.related import ForeignKey


# User model
class GGITUser(AbstractUser):
    settings = models.TextField(blank=True, null=True)



# Note model
class Note(models.Model):
     author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
     title = models.CharField(max_length=200)
     created_date = models.DateTimeField(
            default=datetime.now)
     updated_date = models.DateTimeField(
            blank=True, null=True)

     def updated_date(self):
        self.updated_date = datetime.now()
        self.save()
     
     def __str__(self):
        return "Title:"+ self.title +"\nAuthor:"+self.author


# NoteElement model
class NoteElement(models.Model):
    text = models.TextField(blank=True,null=True)
    ##author=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    note=ForeignKey(Note,on_delete=models.CASCADE)
    image=models.TextField(blank=True,null=True)
    video=models.TextField(blank=True,null=True)
   
    def __str__(self):
        return self.text + self.image +self.video 
   