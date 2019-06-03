from django.urls import path
from . import views
from .views import PostListView, PostCreateView
urlpatterns = [
    path( 'about/', views.about , name='blog-about' ),
    path('view/', PostListView.as_view(), name='view-posts'),
    path('new/', PostCreateView.as_view(), name='create-post'),

]
