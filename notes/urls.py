from django.urls import path
from notes.views import user_views, note_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('users/register/', user_views.register, name='register'),
    path('users/me', user_views.user_me, name='user_me'),
    path('notes', note_views.notes, name='notes'),
    path('users', user_views.all_users, name='all_users'),
    path('users/login', obtain_auth_token, name='login'),
    path('users/is-unique/', user_views.is_unique, name='is_unique'),
    path('users/<int:user_id>/', user_views.user_detail, name='user_detail'),
    path('notes/<int:note_id>/ ', note_views.note_details, name='note_details'),
   
]
