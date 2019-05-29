from django.db import models
import datetime

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Account(models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=150)
    username    = models.CharField(max_length=100)
    email       = models.EmailField(null=True , unique= True)
    roleid      = models.ForeignKey(Role, on_delete= models.CASCADE)
    password    = models.CharField(max_length=15,null=False)
    phone       = models.IntegerField()
    dob         = models.DateField(default=datetime.date.today)
    address     = models.TextField(max_length=150)
    profilepic  = models.TextField(max_length=250)


class Book(models.Model):
    name        = models.CharField(max_length=150)
    Author      = models.CharField(max_length=100)
    Dop         = models.TextField(max_length=100)
    id          = models.IntegerField(primary_key=True)


class Post(models.Model):
    id          = models.IntegerField(primary_key=True)
    title       = models.TextField()
    date        = models.DateField(default=datetime.date.today)
    content     = models.TextField()

class AccountBook(models.Model):
    bookid      = models.ForeignKey(Book , on_delete= models.CASCADE)
    Accountid   = models.ForeignKey(Account , on_delete=models.CASCADE)