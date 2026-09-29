"""URL configuration for the blog app."""
from django.urls import path
from . import views

app_name = 'blog' 

urlpatterns = [
    path('home/',  views.blog_view, name='home'),
    path('<int:pid>/',  views.blog_single_view, name='single'),
    path('category/<str:cat_name>', views.blog_view, name='category'),
    path('author/<str:author_username>', views.blog_view, name='author'),
    path('search/',views.blog_search, name='search'),
    path('test/', views.test, name='test'),
    
]
 