from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="username",max_length=30)
    password= forms.CharField(label="password", max_length=30)

class RegisterForm(forms.Form):
    username = forms.CharField(label="username",max_length=30)
    password= forms.CharField(label="password", max_length=30)
    email = forms.CharField(label="email", max_length=30)
    first_name = forms.CharField(label="first_name", max_length=30)
    last_name = forms.CharField(label="last_name", max_length=30)

class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=20)
    description = forms.CharField(label='Description', max_length=20)
    file = forms.FileField(label='file',required=False)

class CommentForm(forms.Form):
    text = forms.CharField(label='text', max_length=300)
    #video = forms.IntegerField(widget=forms.HiddenInput(), initial=1) 