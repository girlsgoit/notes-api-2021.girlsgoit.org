from django.urls import path
from notes.views import user_views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/register/', user_views.register, name='register'),
    path('user/is-unique/', user_views.is_unique, name='is_unique'),
    path('user/me', user_views.user_me, name='user_me'),
    path('users', user_views.all_users, name='all_users')
]
