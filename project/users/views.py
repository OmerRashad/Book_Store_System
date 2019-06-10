from django.shortcuts import render, redirect
from blog.forms import AccountCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from blog.models import Account
from .models import UserUpdateForm, ProfileUpdateForm, ConfirmationForm
import random
from django.core.mail import send_mail

def signup(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            con = random.randint(1000, 9999)
            user=Account.objects.get(username=request.POST.get('username'))
            email = user.email
            name=user.username
            Account.objects.update(randNum= con)
            msg = 'Hello '+name+', here is your verification code ' + str(con)
            send_mail(
                'Confirmation',
                msg,
                'socialbookstorefcih@gmail.com',
                [email],
                fail_silently=False,
            )

            return redirect('confirmation')
    else:
        form = AccountCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def confirmation(request):
    if request.method == 'POST':
        form = ConfirmationForm(request.POST)
        if form.is_valid():
            username    = form.cleaned_data.get('username')
            code        = form.cleaned_data.get('code')
            # return redirect('omer')

            try:
                user = Account.objects.get(username = username)
                if user.randNum == code:
                    Account.objects.update(confirm = 1)
                    return redirect('login')

                else:
                    return redirect('confirmation')

            except Exception:
                return redirect('omer')
        else:
            form = ConfirmationForm()
    else:
        form = ConfirmationForm()
    return render(request,'users/confirmation.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


def viewHome(request):
    return render(request,'blog/home.html')



def confirm(request):
    if request.method == 'POST':
        form = ConfirmationForm()
        if form.is_valid():
            username    = form.cleaned_data.get('username')
            code        = form.cleaned_data.get('code')
            try:
                user = Account.objects.get(username = username)
                if user.randNum == code:
                    Account.objects.update(confirm = 1)
                    return redirect('omer')

                else:
                    return redirect('confirmation')

            except Exception:
                return redirect('omer')
        else:
            form = ConfirmationForm()
    else:
        form = ConfirmationForm()
    return render(request,'users/confirmation.html',{'form':form})