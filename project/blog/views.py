from django.shortcuts import render , redirect
from django.http import HttpResponse
from blog.models import Account
from blog.models import Role
from django.views.generic import ListView
from .models import Post
from blog.models import PostForm

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = PostForm()
    return render(request, 'users/signup.html', {'form': form})

def home(request):
    context = {
        'posts' : Post
    }
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model=Post
    template_name='blog/home.html'
    context_object_name='posts'
    ordering =['-date']

def about(request):
    return render(request,'blog/about.html' , {'title': 'About'} )
