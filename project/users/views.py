from django.shortcuts import render, redirect
from users.models import AuthorForm
def signup(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')
    else:
        form = AuthorForm()
    return render(request, 'users/signup.html', {'form': form})