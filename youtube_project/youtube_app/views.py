from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from youtube_app.forms import *
from django.contrib.auth import authenticate, login, logout
from youtube_app.models import *
from django.core.files.storage import FileSystemStorage
import os
from wsgiref.util import FileWrapper
import random

import string
# Create your views here.


class HomeView(View):
    template_name = 'youtube_app/index.html'
    def get(self, request):
        most_recent_videos = Video.objects.order_by('-datetime')[:8]
        return render(request, self.template_name, {'menu_active_item': 'home', 'most_recent_videos': most_recent_videos})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')


class LoginView(View):
    template_name = 'youtube_app/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/register/")
            else:
                return HttpResponse("invalid")


class RegisterView(View):
    template_name = 'youtube_app/register.html'
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect("/")
        form = RegisterForm()
        return render(request,self.template_name,{'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username=username,email=email)
            new_user.set_password(password)  # this way it will  save password using some algo
            new_user.save()
        return HttpResponse("JssssssssHGHB")


class NewVideo(View):
    template_name = 'youtube_app/new_video.html'

    def get(self, request):
        print(request.user.is_authenticated)
        if not  request.user.is_authenticated:
            # return HttpResponse('You have to be logged in, in order to upload a video.')
            return HttpResponseRedirect('/register')
        
        form = NewVideoForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        # pass filled out HTML-Form from View to NewVideoForm()
        # user_form = StudentForm(request.POST, request.FILES)
        form1 = NewVideoForm(request.POST, request.FILES)
        print("sjkjh",form1.errors)
        if form1.is_valid():
        	title = form1.cleaned_data['title']
        	description = form1.cleaned_data['description']
        	file1 = form1.cleaned_data['file']
        	print("filename",file1)
        	print(request.FILES['file'].name)
        	# random_char = ''.join(random.sample(string.ascii_uppercase + string.digits, k=10))
        	# path = random_char + str(file1)
        	# print("path",path)
        	new_video = Video(title=title, 
                            description=description,
                            user=request.user,
                            video_file=request.FILES['file'])
        	new_video.save()
            # print("video/{}".format(request.id))
        	return HttpResponseRedirect('/video/{}'.format(new_video.id))
        else:
            return HttpResponse('Your form is not valid. Go back and try again.')

# class VideoView(View):
#     template_name = 'youtube_app/video.html'

#     def get(self, request, id):
#         #fetch video from DB by ID
#         video_by_id = Video.objects.get(id=id)
#         # DoesNotExist 
#         context = {'video':video_by_id}
#         print(request.user)
#         if request.user.is_authenticated:
#             print('user signed in')
#             comment_form = CommentForm()
#             context['form'] = comment_form

#         print(context)
#         return render(request, self.template_name, context)


class VideoView(View):
    template_name = 'youtube_app/video.html'

    def get(self, request, id):
        # fetch video from DB by ID
        video_by_id = Video.objects.get(id=id)
        # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(video_by_id.video_file)
        video_by_id.video_file = 'http://127.0.0.1:8000/media/'+ str(video_by_id.video_file)
        context = {'video':video_by_id}
        
        if request.user.is_authenticated:
            print('user signed in')
            comment_form = CommentForm()
            context['form'] = comment_form

        
        comments = Comment.objects.filter(video__id=id).order_by('-datetime')[:5]
        print(comments)
        context['comments'] = comments
        return render(request, self.template_name, context)



class CommentView(View):
    # template_name = 'youtube_app/video.html'

    def post(self, request):
        # pass filled out HTML-Form from View to CommentForm()
        form = CommentForm(request.POST)
        if form.is_valid():
            # create a Comment DB Entry
            text = form.cleaned_data['text']
            video_id = request.POST['video']
            video = Video.objects.get(id=video_id)
            
            new_comment = Comment(text=text, user=request.user, video=video)
            new_comment.save()
            return HttpResponseRedirect('/video/{}'.format(str(video_id)))
        return HttpResponse('This is Register view. POST Request.')


class VideoFileView(View):
    
    def get(self, request, file_name):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file = FileWrapper(open(BASE_DIR+'/'+file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response
