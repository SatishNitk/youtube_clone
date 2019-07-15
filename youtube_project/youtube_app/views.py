from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from youtube_app.forms import *
from django.contrib.auth import authenticate, login
from youtube_app.models import *
import random

import string
# Create your views here.




class Home(View):
	template_name = "youtube_app/index.html"
	def get(self,request):
		return render(request,self.template_name, {'m':"ssbhss"})


class LoginView(View):
	template_name = 'youtube_app/login.html'

	def get(self,request):
		form = LoginForm()
		return render(request,self.template_name,{'form':form})

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

	def get(self,request):
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
        if request.user.is_authenticated == False:
            #return HttpResponse('You have to be logged in, in order to upload a video.')
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
        	print(title)
        	print(description)
        	print("jhhg",file1)
        	print(request.FILES['file'].name)
        	random_char = ''.join(random.sample(string.ascii_uppercase + string.digits, k=10))
        	path = random_char + "hg" #@request.FILES['file'].name
        	new_video = Video(title=title, 
                            description=description,
                            user=request.user,
                            path=path)
        	new_video.save()
        	return HttpResponse('Your form ihjjjjjjjjjjjjjjjjjs not valid. Go back and try again.')

            # return HttpResponseRedirect('/video/{}'.format(new_video.id))
        else:
            return HttpResponse('Your form is not valid. Go back and try again.')
