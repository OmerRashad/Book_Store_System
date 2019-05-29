from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Account
from blog.models import Role

def home(request):
    context = {
        'posts' : Role.objects.all()
    }
    return render(request,'blog/home.html', context   )

def about(request):
    return render(request,'blog/about.html' , {'title': 'About'} )
