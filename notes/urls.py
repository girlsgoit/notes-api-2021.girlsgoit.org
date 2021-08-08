from django.urls import path
from notes.views import user_views, note_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/register/', user_views.register, name='register'),
    path('user/me', user_views.user_me, name='user_me'),
    path('notes', note_views.post_note, name='post_note'),
    path('user/is-unique/', user_views.is_unique, name='is_unique'),
    path('user/<int:user_id>/', user_views.user_detail, name='user_detail'),
    path('notes/<int:note_id>/ ',note_views.note_details,name='note_details'),
]
