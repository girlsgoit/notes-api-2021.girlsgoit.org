from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'is_superuser', 'last_login']
