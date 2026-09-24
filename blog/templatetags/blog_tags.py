from django import template
from blog.models import Post

register = template.Library() 


@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def function():
    posts = Post .objects.filter(status=1)
    return posts



@register.filter
def snippet(value,arg=20):
    return value[:arg] + '...'


@register.inclusion_tag('blog/blog_popular_posts.html', name='popularposts')
def latest_post():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:1]
    return {'posts':posts}
