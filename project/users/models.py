from django.db import models
from django.forms import ModelForm
from blog.models import Account

class AuthorForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'username', 'email','roleid','password','phone','dob','address','profilepic']