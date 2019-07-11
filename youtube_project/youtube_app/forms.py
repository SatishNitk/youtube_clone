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
