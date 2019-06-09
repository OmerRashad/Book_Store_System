from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Book

class AddBook(CreateView):
    model = Book
    template_name = 'store/store.html'
    fields = ['name', 'author', 'dop', 'sale','ispn','description','price','copies']

    # This Line Is For Redirect To Home After Adding A New Post
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ViewBook(ListView):
    model=Book
    template_name='store/shop.html'
    context_object_name='books'

