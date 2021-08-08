from django.urls import path
from notes.views import user_views, post_note
from ..views import user_me
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/register/', user_views.register, name='register'),
    path('user/me', user_me, name='user_me'),
    path('notes', post_note, name='post_note'),
    path('user/is-unique/', user_views.is_unique, name='is_unique'),
]
