from django.urls import path
from .views import AddBook, ViewBook
urlpatterns = [
    path('new/', AddBook.as_view(), name='add-book'),
    path('shop/',ViewBook.as_view(), name='view-book')
]