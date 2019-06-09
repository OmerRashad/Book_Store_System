from django.conf.urls import url
from django.urls import path
from .views import AddBook, ViewBook,book_profile
urlpatterns = [
    path('new/', AddBook.as_view(), name='add-book'),
    path('shop/',ViewBook.as_view(), name='view-book'),
    path('book_profile/<int:pk>/',book_profile.as_view(),name='book_profile')
]