
from django.urls import path,include
from youtube_app.views import *
urlpatterns = [
    path('',home, name="ss"),
]
