from django.db import models
from django import forms
from PIL import Image


# Create your models here.
import datetime
from blog.models import Account
from users.models import Profile, Book


class OrderItem(models.Model):
    product = models.ForeignKey(Book, on_delete = models.CASCADE, null = True)
    is_ordered = models.BooleanField(default = True, null = True)
    date_ordered = models.DateTimeField(null = True)
    date_added = models.DateTimeField(auto_now = True, null = True)
    amount = models.IntegerField(default = 1, null = True)

    def __str__(self):
        return self.product.name


class Order(models.Model):
    id              = models.AutoField(primary_key=True)
    ref_code        = models.CharField(max_length = 15, null = True)
    date_ordered    = models.DateTimeField(auto_now = True, null = True)
    is_ordered       = models.BooleanField(default = False, null = True)
    items           = models.ManyToManyField(OrderItem)
    owner           = models.ForeignKey(Profile,on_delete = models.CASCADE, null = True)

    def get_cart_items(self):
        return self.items.all()
    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return '{0}-{1}'.format(self.owner, self.ref_code)


class Book_Profile(models.Model):
    book        = models.OneToOneField(Book,on_delete=models.CASCADE)
    image       = models.ImageField(default='default.jpg', upload_to='book_pics')
    # def save(self):
    #     super(Book_Profile, self).save()
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (500,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

class AccountBook(models.Model):
    bookid      = models.ForeignKey(Book , on_delete= models.CASCADE)
    Accountid   = models.ForeignKey(Account , on_delete=models.CASCADE)

class SearchForm(forms.Form):
    search_content  = forms.CharField(max_length=20)
