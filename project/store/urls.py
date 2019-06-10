from django.conf.urls import url
from django.urls import path
from .views import AddBook,book_profile,addToLikes,ViewLikes
from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    success,
    book_list)
app_name = "store"

urlpatterns = [
    path('new/', AddBook.as_view(), name='add-book'),
    path('shop/',book_list, name='book'),
    path('book_profile/<int:pk>/',book_profile.as_view(),name='book_profile'),
    path('addtolikes/(?P<book>\w+)/$',addToLikes,name='addToLikes' ),
    path('likes/', ViewLikes.as_view(), name='view-likes'),
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^update-transaction/(?P<token>[-\w]+)/$', update_transaction_records, name='update_records')
]

