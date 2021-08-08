from django.urls import path
from notes.views import user_views

urlpatterns = [
    path('user/register/', user_views.register, name='register'),
]