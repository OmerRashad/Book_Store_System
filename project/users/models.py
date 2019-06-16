import datetime

from django.db import models
from django import forms
from blog.models import Account


class Category(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Book(models.Model):
    name        = models.CharField(max_length=150)
    author      = models.CharField(max_length=100)
    dop         = models.DateField(default=datetime.date.today)
    id          = models.IntegerField(primary_key=True)
    owner       = models.ForeignKey(Account,on_delete=models.CASCADE)
    sale        = models.IntegerField()
    ispn        = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    price       = models.IntegerField()
    copies      = models.IntegerField(default=1)
    rate        = models.FloatField(default=0,null=True)
    cover       = models.ImageField(default = 'empty_cover.png',upload_to = 'book_pics', null = True)
    category    = models.ForeignKey(Category, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.name

    def get_sale(self):
        return (self.price * (self.sale / 100))


class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    ebooks = models.ManyToManyField(Book, blank = True , null = True)

    def __str__(self):
        return self.user.username


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Account
        fields = ['username', 'email' ,'address']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class ConfirmationForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    username    = forms.CharField(max_length = 20)
    code        = forms.IntegerField()
    #All my attributes here

