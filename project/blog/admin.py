from django.contrib import admin
from blog.models import Account
from blog.models import Post
from blog.models import Book
from blog.models import Role
from blog.models import AccountBook


admin.site.register(Account)
admin.site.register(Book)
admin.site.register(Post)
admin.site.register(Role)
admin.site.register(AccountBook)


# Register your models here.
