from django.contrib import admin

from users.models import Category
from .models import Book,Book_Profile,AccountBook,OrderItem,Order


# Register your models here.
admin.site.register(Book)
admin.site.register(Book_Profile)
admin.site.register(AccountBook)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)

