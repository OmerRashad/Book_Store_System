import datetime

from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView

from store.extras import generate_order_id
from .models import SearchForm
from store.models import Book, Order, OrderItem
from users.models import Profile
from .models import AccountBook
from blog.models import Account
from django.contrib.auth.decorators import login_required
from django.contrib import messages

class AddBook(CreateView):
    model = Book
    template_name = 'store/store.html'
    fields = ['name', 'author', 'dop', 'sale','ispn','description','price','copies','cover','category']

    # This Line Is For Redirect To Home After Adding A New Post
    success_url = reverse_lazy('blog-home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ViewBook(ListView):
    model=Book
    template_name='store/shop.html'
    context_object_name='books'

class ViewLikes(ListView):
    model=AccountBook
    template_name='store/likes.html'
    context_object_name='Accountbooks'

class book_profile(DetailView):
    model = Book
    template_name = "store/book_profile.html"

def addToLikes(request,book):
    book_id = Book.objects.get(id = book)
    user = Account.objects.get(username = request.user.username)
    AccountBook.objects.create(bookid=book_id,Accountid=user)
    return redirect('blog-home')


@login_required()
def book_list(request):
    object_list = Book.objects.all()
    filtered_orders = Order.objects.filter(owner = request.user.profile, is_ordered=False)
    current_order_products = []
    if filtered_orders.exists():
        user_order = filtered_orders[0]
        user_order_items = user_order.items.all()
        current_order_products = [product.product for product in user_order_items]

    context = {
        'object_list': object_list,
        'current_order_products': current_order_products
    }

    return render(request, "store/shop.html", context)


@login_required()
def get_user_pending_order(request):
    user_profile = get_object_or_404(Profile ,user=request.user)
    order = Order.objects.filter(owner=user_profile, is_ordered=False)
    if order.exists():
        return order[0]
    return 0


@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = get_object_or_404(Profile, user=request.user)
    # filter products by id
    product = Book.objects.filter(id=kwargs.get('item_id', "")).first()
    # check if the user already owns this product
    if product in request.user.profile.ebooks.all():
        messages.info(request, 'You already own this ebook')
        return redirect(reverse('store:book'))
    # create orderItem of the selected product
    order_item, status = OrderItem.objects.get_or_create(product=product)
    # create order associated with the user
    user_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('store:book'))


@login_required()
def delete_from_cart(request,item_id):
    item_to_delete = OrderItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request,"Item has been deleted")
    return redirect(reverse('store:order_summary'))


@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request,'store/order_summary.html',context)


@login_required()
def checkout(request):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order,
    }
    return render(request, 'store/checkout.html', context)



@login_required()
def process_payment(request , order_id):
    return redirect(reverse('store:update_records',kwargs ={
        'order_id':order_id})
                    )


@login_required()
def update_transaction_records(request, order_id):
    order_to_purchase = Order.objects.filter(pk=order_id).first()
    order_to_purchase.is_orderd = True
    order_to_purchase.date_order = datetime.datetime.now()
    order_to_purchase.save()

    order_items = order_to_purchase.items.all()
    order_items.update(is_ordered = True, date_ordered = datetime.datetime.now())
    user_profile = get_object_or_404(Profile,user=request.user)

    order_products = [item.product for item in order_items]

    user_profile.ebooks.add(*order_products)

    user_profile.save()
    messages.info(request, " Thank you! Your Items have been added to your profile")
    return redirect(reverse('store:book'))


def success(request, **kwargs):
    return render(request, 'store/purchase_success.html',{})

def search_bassem(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            request.session['search_content'] = request.POST['search_content']
            return redirect('store:search2')
    return render(request, 'store/search.html',{})




def transactions(request):
    profile = Profile.objects.all()
    request.session['username'] = request.user.username
    return render(request,"store/transactions.html",{'profiles':profile})


class Search(ListView):
    model = Book
    template_name = 'store/search2.html'
    context_object_name = 'Book'
    # success_url = reverse_lazy('searchh')
