from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from youtube_app.forms import *
from django.contrib.auth import authenticate, login
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
