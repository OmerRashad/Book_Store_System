from django.shortcuts import render, redirect
from blog.forms import AccountCreationForm


def signup(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = AccountCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')


def viewHome(request):
    return render(request,'blog/home.html')
