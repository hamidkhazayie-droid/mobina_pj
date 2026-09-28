"""Views for the blog application."""

from django.shortcuts import render,get_object_or_404
from .models import Post

def blog_view(request,cat_name=None,author_username=None):
    posts = Post.objects.filter(status=True)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username = author_username)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request,pid):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post,
               'posts':posts}
    return render(request, 'blog/blog-single.html', context)
 
 
def test(request):
    return render(request, 'test.html') 


def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render (request,'blog/blog-home.html',context)
    
