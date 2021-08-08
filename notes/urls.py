from django.urls import path
from notes.views import user_views
from ..views import user_me
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/register/', user_views.register, name='register'),


    path('user/me', user_me, name='user_me'),
]
