"""Views for the blog application."""

from django.shortcuts import render,get_object_or_404
from .models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single_view(request,pid):
    posts = Post.objects.all()
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post,
               'posts':posts}
    return render(request, 'blog/blog-single.html', context)
 
def media_view(request):
    context = {
        'name':'mobina',
        'email':'mobina@khazayie',
        'bio':'tuf gaming'
    }
    return render (request, 'blog/media.html', context)


def test(request,pid):
    # post = get_object_or_404(Post, id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request, 'test.html',context)


