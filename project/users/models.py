from django.db import models
from django.forms import ModelForm
from django import forms
from blog.models import Account,Post,Book
from django.contrib.auth import authenticate

from django.contrib.auth.forms import AuthenticationForm , User, UsernameField


class AuthorForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'username', 'email','roleid','password','phone','dob','address','profilepic']

class ReaderForm(ModelForm):
    class Meta:
        model = Book
        fields = ['Author','name','Dop']

class WriterForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','date','content']

class Login(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(max_length=100)
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput,
    )
