from django.contrib.auth.models import User
from django.db import models
import datetime
from django.forms import ModelForm
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Account(AbstractUser):
    # id          = models.AutoField(primary_key=True )
    roleid      = models.ForeignKey(Role, on_delete= models.CASCADE,blank=True,null = True)
    dob         = models.DateField(default=datetime.date.today)
    address     = models.TextField(max_length=150,null=True)
    confirm     = models.IntegerField(default = 0,null = True)
    randNum     =models.IntegerField(default=0, null=True)


class Book(models.Model):
    name        = models.CharField(max_length=150)
    Author      = models.CharField(max_length=100)
    Dop         = models.TextField(max_length=100)
    id          = models.IntegerField(primary_key=True)


class Posts(models.Model):
    id          = models.IntegerField(primary_key=True)
    title       = models.TextField()
    date        = models.DateTimeField(default=timezone.now)
    content     = models.TextField()
    name        = models.CharField(max_length=100)
    def __str__(self):
        return self.title



class PostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content']

