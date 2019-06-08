from django.db import models

# Create your models here.
import datetime
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
    #cover       = models.ImageField(default='default.jpg',upload_to='book_pics')
    ispn        = models.CharField(max_length=100)
    # category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    price       = models.IntegerField()
    copies      = models.IntegerField(default=1)
    rate        = models.FloatField(default=0,null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    id          = models.AutoField(primary_key=True)
    user_id     = models.ForeignKey(Account,on_delete=models.CASCADE)
    data        = models.DateTimeField(default=datetime.datetime.now)


class OrderItem(models.Model):
    order_id    = models.ForeignKey(Order,on_delete=models.CASCADE)
    product_id  = models.ForeignKey(Book,on_delete=models.CASCADE)
    id          = models.AutoField(primary_key=True)
    amount      = models.IntegerField(default=1)


class Book_Profile(models.Model):
    book        = models.OneToOneField(Book,on_delete=models.CASCADE)
    image       = models.ImageField(default='default.jpg', upload_to='book_pics')