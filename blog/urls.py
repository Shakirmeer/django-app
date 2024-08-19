from django.urls import path
from . import views
from .views import PostListView, DetailListView, CreateListView, UpdateListView, DeleteListView

urlpatterns = [
    path('',PostListView.as_view() , name='blog-home'),
    path('post/<int:pk>',DetailListView.as_view() , name='post-detail'),
    path('post/new',CreateListView.as_view() , name='post-create'),
    path('post/<int:pk>/update',UpdateListView.as_view() , name='post-update'),
    path('post/<int:pk>/delete',DeleteListView.as_view() , name='post-delete'),
    path('about/', views.about, name='about'), 
    path('disclaimer/', views.disclaimer, name='blog-disclaimer'),
    path('contactus/', views.contactus, name='contact'),
]
