from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account,Comment


class AccountCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Account
        fields = ( 'username', 'email','roleid','password1','password2','dob','address')

class AccountChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email')


