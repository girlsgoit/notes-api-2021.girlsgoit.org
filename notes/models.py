from django.contrib.auth.models import AbstractUser
from django.db import models


# User model
class GGITUser(AbstractUser):
    settings = models.TextField(blank=True, null=True)






# Note model







# NoteElement model
