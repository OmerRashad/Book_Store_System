from django.db import models
from django.forms import ModelForm
from django import forms
from blog.models import Account,Posts,Book
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm , User, UsernameField
from blog.forms import AccountCreationForm

class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

class ReaderForm(ModelForm):
    class Meta:
        model = Book
        fields = ['Author','name','Dop']

class WriterForm(ModelForm):
    class Meta:
        model = Posts
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

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email' ,'address']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']