from django.urls import path

from .views import profile_view, my_olympiad_view

app_name = 'accounts'
urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('my-olympiads/', my_olympiad_view, name='my_olympiad'),
]