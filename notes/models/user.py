from django.contrib.auth.models import AbstractUser
from django.db import models

class GGITUser(AbstractUser):
    settings = models.TextField(blank=True, null=True)
