"""URL configuration for the blog app."""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('home/',  views.blog_view, name='home'),
    path('media/', views. media_view, name='media'),
    path('category/<str:cat_name>', views.blog_category, name='category'),
    path('test/', views.test, name='test'),
    path('<int:pid>/',  views.blog_single_view, name='single'),
]
