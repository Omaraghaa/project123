from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    #path('msteams/', views.sign_in, name='msteams'),
    path('chat/', views.chat, name='chat'),
    #path('callback/', views.callback, name='callback'),
    path('contact/',views.contact, name='blog-contact'),
    path('xhome/', views.xhome, name='blog-xhome'),
     path('aboutus/', views.aboutus, name='blog-about'),
     
]
