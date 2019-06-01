from django.core import serializers
from django.shortcuts import render, redirect
from users.models import AuthorForm

from blog.models import Account

from users.models import Login


def signup(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            data = request.POST.get("roleid")
            form.save()

            if data == "2":
                return redirect('blog-home')
            if data == "3":
                return redirect('omer')

    else:
        form = AuthorForm()
    return render(request, 'users/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            try:
                account = Account.objects.get(username=username,password = password)

                if account:
                    request.session['type'] = 2
                    request.session['name'] = account.name
                    is_authenticated(request,username)
                    return redirect('blog-home')

            except Exception:
                return redirect('login')
    else:
        form = Login()
    return render(request, 'users/login.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')


def logout(request):
    is_authenticated(request,username="")
    return render(request,'users/logout.html')


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