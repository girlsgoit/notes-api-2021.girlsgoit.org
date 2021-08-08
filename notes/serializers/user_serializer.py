from rest_framework.serializers import ModelSerializer
from ..models import GGITUser
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = GGITUser
        exclude = ['password', 'is_superuser', 'last_login']
        