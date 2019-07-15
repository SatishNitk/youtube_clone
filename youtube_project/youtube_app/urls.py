
from django.urls import path,include
from youtube_app.views import *

urlpatterns = [
 	path('', Home.as_view()),
    path('login/',LoginView.as_view()),
    path('register/',RegisterView.as_view()),
    path('video/',NewVideo.as_view()),
    



]
