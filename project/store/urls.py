from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddBook,book_profile,addToLikes,ViewLikes,Search,search_bassem
from .views import (
    add_to_cart,
    delete_from_cart,
    order_details,
    checkout,
    update_transaction_records,
    success,
    book_list,process_payment,transactions)
app_name = "store"

urlpatterns = [
    path('new/', AddBook.as_view(), name='add-book'),
    path('shop/',book_list, name='book'),
    path('book_profile/<int:pk>/',book_profile.as_view(),name='book_profile'),
    path('addtolikes/<book>/',addToLikes,name='addToLikes' ),
    path('likes/', ViewLikes.as_view(), name='view-likes'),
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^checkout/$', checkout, name='checkout'),
    url(r'^transactions/$', transactions, name='transactions'),
    url(r'^update-transaction/(?P<order_id>[-\w]+)/$', update_transaction_records, name='update_records'),
    url(r'^payment/(?P<order_id>[-\w]+)/$', process_payment, name='process_payment'),
    path('search/',search_bassem,name='search'),
    path('searchh/',Search.as_view(),name='search2'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
