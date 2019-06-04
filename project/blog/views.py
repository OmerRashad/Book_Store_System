from django.shortcuts import render , redirect
from django.http import HttpResponse
from blog.models import Account
from blog.models import Role
from django.views.generic import ListView, CreateView
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
        'posts' : Role.objects.all(),'accounts': Account.objects.all()
    }
    return render(request,'blog/home.html', context)

class PostListView(ListView):
    model=Post
    template_name='blog/blogPosts.html'
    context_object_name='posts'
    ordering =['-date']

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self,form):

        form.instance.name = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request,'blog/about.html' , {'title': 'About'} )
