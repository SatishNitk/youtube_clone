
from django.urls import path,include
from youtube_app.views import *

urlpatterns = [
 	path('', HomeView.as_view()),
    path('login/',LoginView.as_view()),
    path('register/',RegisterView.as_view()),
    path('video/',NewVideo.as_view()),
    path('logout/',LogoutView.as_view()),
    path('comment/',CommentView.as_view()),
    path('video/<int:id>', VideoView.as_view()),
    path('get_video/<file_name>', VideoFileView.as_view()),
] 
