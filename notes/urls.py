from django.urls import path
from notes.views import user_views
from ..views import user_me, user_detail, register
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/register/', register, name='register'),
    path('user/<int:user_id>/', user_detail, name='user detail'),

    path('user/me', user_me, name='user_me'),
]
