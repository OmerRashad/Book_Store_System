from django.contrib.auth.models import User
from django.core import serializers
from django.shortcuts import render, redirect
from users.models import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages


from blog.models import Account

from users.models import Login



def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = request.POST.get("roleid")
            form.save()

            if data == "2":
                return redirect('blog-home')
            if data == "3":
                return redirect('blog-home')

    else:
        form = UserForm()
    return render(request, 'users/signup.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         form = Login(request.POST)
#         if form.is_valid():
#             username = request.POST.get("username")
#             password = request.POST.get("password")
#             try:
#                 account = Account.objects.get(username = username)
#                 path = request.get_full_path()
#                 if account:
#                     # request.session['type'] = request.roleid.id
#                     # request.session['name'] = request.name
#                     # request.session['user_id'] = request.id
#                     is_authenticated(request,username)
#                     return redirect('blog-home')
#             except Exception:
#                 return redirect('login')
#     else:
#         form = Login()
#     return render(request, 'users/login.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('blog-home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "users/login.html",
                    context={"form":form})


def profile(request):
    return render(request, 'users/profile.html')


def logout(request):
    is_authenticated(request,username="")
    return render(request,'blog/home.html')


def viewHome(request):
    return render(request,'blog/home.html')

def is_authenticated(request,username):
    if username:
        #request.session['type'] = ""
        request.session["is_authenticated"] = True
 #       get_user_data(request,username)
    else:
        request.session["is_authenticated"] = False



'''def get_user_data(request,username):
    account = Account.objects.get(username=username)
    serialized_obj = serializers.serialize('json', [account, ])
    request.session["user_data"] = serialized_obj
'''

